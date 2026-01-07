# async  with coroutine a special feature that the function can be paused
# await pause the execution until the result is ready
# asyncio build in python library
# Event Loop that runs and schedule coroutine in functions
import asyncio


async def brew_chai():
    await print('Ready ')


# by default django and flask or synchronous and blocking in nature where as a fast api is asychrounous
# asychornous is nothing but runnning  a process in single core while sleeping it switch in threads
# nodejs - asyc - give to libuv /OS thread processing - once doen return
# python - async - no libuv /handles switch with same thread - and return
# nodejs - execute autmoaticalu
# python - we need create a async and it return a obj that need to furthur call for execute .
# function created by async is a goroutine and returend object is coroutine object we need to call for executing.

# if we want to handle the thread grace fully in I/0 operations

# asyncio handles the I/O cuncurrent without disturbing we need to create a thread that should run

from concurrent.futures import ThreadPoolExecutor  #basically have the collection of thread that runs on anotther thread maintianing
from concurrent.futures import ProcessPoolExecutor  # same for the creating multiple core processing


def blocking_io():
    print('Fetching or doing some work for a worker')
    return None


async def my_process():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor as pool:
        return await loop.run_in_executor(pool, blocking_io)


#! client request a I/O the asycio i do it with asycn and await mean while we need to a heavy lifting task we use the threadpool or processpool and send them to another thread run , the current user wait for response. if come another user ask the same again we async I/o go take same process
# if process:
# if __name__ == "__main__":  Process it is important
asyncio.run(my_process)

# Demon and non-demon :
# Demon thread are backround thrasynciead it automaticaly shutdown when the server stops;
# non Demon thread are run continously.
