from ultralytics import YOLO



if __name__ == '__main__':
    # 初始化YOLO模型
    model = YOLO('yolov8n.pt')

    # 設置訓練參數
    data = "data.yaml"
    epochs = 100
    batch_size = 64

    # 訓練模型
    results = model.train(data=data, epochs=epochs, batch=batch_size, device=0)

    # Validate the model
    results = model.val(data=data)  # no arguments needed, dataset and settings remembered
