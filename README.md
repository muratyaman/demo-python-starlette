# demo-python-starlette
Demo HTTP server using Python, Starlette and Uvicorn

## installation

```
pip3 install uvicorn
pip3 install starlette
```

## execution

```
uvicorn main:app --no-access-log
```

## references

### Python

"Python is a programming language that lets you work quickly
and integrate systems more effectively."

[https://www.python.org/](https://www.python.org/)

### Starlette

"Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services."

[https://www.starlette.io/](https://www.starlette.io/)


### Uvicorn

"Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools."

[http://www.uvicorn.org/](http://www.uvicorn.org/)

## benchmark

Install autocannon.

[https://github.com/mcollina/autocannon](https://github.com/mcollina/autocannon)

```
npm i -g autocannon
```

Run autocannon using 10 connections for 60 seconds.

```
autocannon -c 10 -d 60 http://127.0.0.1:8000
```

Output:

```
Running 60s test @ http://127.0.0.1:8000
10 connections

┌─────────┬──────┬──────┬───────┬──────┬─────────┬─────────┬──────────┐
│ Stat    │ 2.5% │ 50%  │ 97.5% │ 99%  │ Avg     │ Stdev   │ Max      │
├─────────┼──────┼──────┼───────┼──────┼─────────┼─────────┼──────────┤
│ Latency │ 0 ms │ 0 ms │ 0 ms  │ 1 ms │ 0.03 ms │ 0.21 ms │ 10.26 ms │
└─────────┴──────┴──────┴───────┴──────┴─────────┴─────────┴──────────┘
┌───────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│ Stat      │ 1%      │ 2.5%    │ 50%     │ 97.5%   │ Avg     │ Stdev   │ Min     │
├───────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Req/Sec   │ 10487   │ 11303   │ 16399   │ 16607   │ 15856   │ 1337.76 │ 10484   │
├───────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Bytes/Sec │ 1.54 MB │ 1.66 MB │ 2.41 MB │ 2.44 MB │ 2.33 MB │ 197 kB  │ 1.54 MB │
└───────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘

Req/Bytes counts sampled once per second.

951k requests in 60.05s, 140 MB read
```
