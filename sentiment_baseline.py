import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import argparse

def main():
    parser = argparse.ArgumentParser(description="Load and display information about CSV files.")
    args = parser.parse_args()

    data_df = pandas.read_csv("./sentiment_test/bow_model.csv")
    label_df = pandas.read_csv("./sentiment_test/sentiment_label.csv")

    features = data_df.columns[:]
    label = label_df.columns[0]

    X = data_df[features]
    y = label_df[label]

    print(X.head(10))
    print(y.head(10))

    # 使用train_test_split随机划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=39583266)  # 20%的数据作为测试集

    # 初始化LogisticRegression模型
    logistic_regression = LogisticRegression(max_iter=10000)

    # 训练模型
    logistic_regression.fit(X_train, y_train)

    # 预测测试集
    predictions = logistic_regression.predict(X_test)

    # 计算并打印准确率
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.2f}")

    df = pandas.read_csv("result.csv")
    new_data = {'Dataset': "sentiment_base", 'Dim': 100, 'DimDBOW': -1, "DimDM": -1, "Accuracy": f"{accuracy:.2f}"}
    df = df._append(new_data, ignore_index=True)
    df.to_csv("result.csv", index=False)

if __name__ == "__main__":
    main()