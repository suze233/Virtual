from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 模拟模型数据
model_data = {
    "Mao": {
        "name": "Mao",
        "path": "/static/Live2D/live2d-model/Mao/Mao.model3.json"
    },
    "miku": {
        "name": "Miku",
        "path": "/static/Live2D/live2d-model/miku/miku.model3.json"
    },
    "Hiyori": {
        "name": "Hiyori",
        "path": "/static/Live2D/live2d-model/Hiyori/Hiyori.model3.json"
    },
    "Haru": {
        "name": "Hary",
        "path": "/static/Live2D/live2d-model/Haru/Haru.model3.json"
    },
    "tororo": {
        "name": "Tororo",
        "path": "/static/Live2D/live2d-model/tororo/tororo.model3.json"
    }
    # 添加更多模型数据
}

app = FastAPI()
origins = [
    "*"  # 允许前端应用的来源
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {"hello world!"}


@app.get('/get_live2d_list')
def get_models():
    return list(model_data.keys())


# @app.get('/load_model')
# def load_model():
#     model_name = request.args.get('model')
#     model = model_data.get(model_name)
#     return jsonify(model)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
