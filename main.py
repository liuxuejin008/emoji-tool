
if __name__ == '__main__':
    import uvicorn
    port = 8080  # 将端口号转换为整数

    #railway启动
    uvicorn.run(app='index:app', host="0.0.0.0", port=port)
    #本地启动
    #uvicorn.run(app='main:app', host="0.0.0.0", port=port)
