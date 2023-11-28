> 根据规则自动抢vast设备并注入挖矿脚本

## 用法

1. 下载仓库: `git clone https://github.com/Dylanma1994/xen-block-vast-miner`
2. 安装python依赖文件: `pip install -U -r requirements.txt`
3. 打开config.json文件配置信息，配置信息
```
{
  "url": "https://console.vast.ai", # vastai地址，不需要更改
  "vast_api_key": "xxx", # 填写vast的api key，在这里可以看到
  "eth_address": "xxx", # 小狐狸钱包地址，直接复制过来
  "machine_configs": [ # 需要抢的设备信息，可以配置多个
    {
      "gpu_name": "RTX_3090", # GPU名字
      "gpu_nums": 2, # GPU数量
      "dph": 0.5, # 每小时金额上限
      "cuda_compute": 89, # cuda算力值，在这里可以找到GPU对应的算力: https://developer.nvidia.com/cuda-gpus#compute
      "machine_nums": 1 # 需要抢几台
    }
  ]
}
```
4. 运行脚本: `python3 shell_miner.py`

