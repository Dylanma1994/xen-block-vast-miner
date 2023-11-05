apt update && apt upgrade -y
apt install git cmake make ocl-icd-opencl-dev python-is-python3 pip screen -y
git clone https://github.com/shanhaicoder/XENGPUMiner.git
cd XENGPUMiner
chmod +x ./build.sh
./build.sh  -cuda_arch sm_$CUDA_COMPUTE
pip install -U -r requirements.txt
sed -i "5d" config.conf
sed -i "5i\account = $ETH_ADDRESS" config.conf

nohup python3 miner.py --gpu=true > miner.log 2>&1 &
count=0
while [ $count -lt $GPU_NUMS ]; do echo "screen -dmS miner$count ./xengpuminer -d $count"; screen -dmS miner$count ./xengpuminer -d $count; let count++; done