from langchain.chat_models import init_chat_model
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START,END
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt ,Command

from dotenv import load_dotenv
load_dotenv()



class State(TypedDict):
    # Messages have the type 'list' . the 'add_messages function'
    # inthe annotaion defines how this state ky should be updated
    # (in this case , it appends messages to the list, ratehr than overwriting them)
    messages: Annotated[list, add_messages]


@tool
def get_stock_price(symbol:str) ->float:
    '''Return the current price of a stock given the stock symbol
    :parma symbol: stock symbol
    :return: current price to the stock
    '''
    return {
        'MSFT':234.4,
        'AAPL':323.4,
        'AMZN':324.4,
        'RIL':45.3,
    }.get(symbol,0.0)

@tool
def buy_stocks(symbol:str,quantity:int,total_price:float)->str:
    '''buy stocks give the stock symbol and quantity'''
    decision = interrupt(f'Approve buying {quantity} {symbol} stocks for ${total_price:.2f}?')
    if decision =='yes':
        return f'You bought {quantity} shares of {symbol} for a total of {total_price}'
    else:
        return 'Buying declined'

tools = [get_stock_price,buy_stocks]


llm = init_chat_model('google_genai:gemini-2.0-flash')
llm_with_tools = llm.bind_tools(tools)

def chatbot_node(state: State):
    msg = llm_with_tools.invoke(state['messages'])
    return {"messages":[msg]}


memory = MemorySaver()
builder = StateGraph(State)
builder.add_node("chatbot",chatbot_node)
builder.add_node('tools',ToolNode(tools))
builder.add_edge(START,'chatbot')
builder.add_conditional_edges('chatbot',tools_condition)
builder.add_edge('tools','chatbot')
builder.add_edge('chatbot',END )
graph = builder.compile(checkpointer=memory)


config = {'configurable':{'thread_id':'buy_thread'}}

#Step 1: user asks price
state = graph.invoke({'messages':[{'role':'user','content':'what is the current price of  AAPL stocks?'}]},config = config)
print(state['messages'][-1].content)

state = graph.invoke({'messages':[{'role':'user','content':"Buy 10 AAPL stock at current price"}]},config = config)
print(state.get('__interrupt__'))


decision = input('Approve (yes/no): ')
state = graph.invoke(Command(resume=decision),config=config)
print(state['messages'][-1].content)













