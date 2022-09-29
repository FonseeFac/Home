from asyncio.windows_events import NULL


def iva(fact, iv):
    if iv == NULL :
        return fact*1.21
    else:
        return fact*((iv/100)+1)


print(iva(100,10))