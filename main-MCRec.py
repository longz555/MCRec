from src.MCRec import train
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # parser.add_argument('--dataset', type=str, default='music', help='数据集')
    # parser.add_argument('--lr', type=float, default=1e-3, help='学习率')
    # parser.add_argument('--l2', type=float, default=1e-4, help='L2正则化系数')
    # parser.add_argument('--batch_size', type=int, default=1024, help='批量大小')
    # parser.add_argument('--epochs', type=int, default=20, help='迭代次数')
    # parser.add_argument('--device', type=str, default='cuda:0', help='设备')
    # parser.add_argument('--embedding_dim', type=int, default=32, help='嵌入维度')
    # parser.add_argument('--predict_factor_dim', type=int, default=32, help='预测因子维度')
    # parser.add_argument('--p', type=int, default=8, help='路径数量')
    # parser.add_argument('--ratio', type=float, default=1, help='训练集使用比例')
    # parser.add_argument('--topk', type=int, default=10, help='top K')

    # parser.add_argument('--dataset', type=str, default='book', help='数据集')
    # parser.add_argument('--lr', type=float, default=1e-3, help='学习率')
    # parser.add_argument('--l2', type=float, default=1e-4, help='L2正则化系数')
    # parser.add_argument('--batch_size', type=int, default=1024, help='批量大小')
    # parser.add_argument('--epochs', type=int, default=20, help='迭代次数')
    # parser.add_argument('--device', type=str, default='cuda:0', help='设备')
    # parser.add_argument('--embedding_dim', type=int, default=32, help='嵌入维度')
    # parser.add_argument('--predict_factor_dim', type=int, default=32, help='预测因子维度')
    # parser.add_argument('--p', type=int, default=8, help='路径数量')
    # parser.add_argument('--ratio', type=float, default=1, help='训练集使用比例')
    # parser.add_argument('--topk', type=int, default=10, help='top K')

    # parser.add_argument('--dataset', type=str, default='ml', help='数据集')
    # parser.add_argument('--lr', type=float, default=1e-2, help='学习率')
    # parser.add_argument('--l2', type=float, default=1e-4, help='L2正则化系数')
    # parser.add_argument('--batch_size', type=int, default=1024, help='批量大小')
    # parser.add_argument('--epochs', type=int, default=20, help='迭代次数')
    # parser.add_argument('--device', type=str, default='cuda:0', help='设备')
    # parser.add_argument('--embedding_dim', type=int, default=32, help='嵌入维度')
    # parser.add_argument('--predict_factor_dim', type=int, default=32, help='预测因子维度')
    # parser.add_argument('--p', type=int, default=8, help='路径数量')
    # parser.add_argument('--ratio', type=float, default=1, help='训练集使用比例')
    # parser.add_argument('--topk', type=int, default=10, help='top K')

    parser.add_argument('--dataset', type=str, default='yelp', help='数据集')
    parser.add_argument('--lr', type=float, default=5e-3, help='学习率')
    parser.add_argument('--l2', type=float, default=1e-4, help='L2正则化系数')
    parser.add_argument('--batch_size', type=int, default=1024, help='批量大小')
    parser.add_argument('--epochs', type=int, default=20, help='迭代次数')
    parser.add_argument('--device', type=str, default='cuda:0', help='设备')
    parser.add_argument('--embedding_dim', type=int, default=32, help='嵌入维度')
    parser.add_argument('--predict_factor_dim', type=int, default=32, help='预测因子维度')
    parser.add_argument('--p', type=int, default=8, help='路径数量')
    parser.add_argument('--ratio', type=float, default=1, help='训练集使用比例')
    parser.add_argument('--topk', type=int, default=10, help='top K')

    args = parser.parse_args()

    train(args, True)
