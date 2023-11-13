# test config.json load and parse
import json, time
from vast import VastClient
from loguru import logger
from threading import Thread

with open("config.json") as j:
    cfg = json.load(j)

flag = False
url = cfg['url']
api_key = cfg['vast_api_key']
eth_address = cfg['eth_address']
machine_configs = cfg['machine_configs']
client = VastClient(api_key=api_key, url=url)


def search_offers(c):
    global flag, eth_address
    try:
        offers = client.search_offers(
            search_query=f'num_gpus = {c["gpu_nums"]} dph <= {c["dph"]} gpu_name = {c["gpu_name"]} '
                         'cuda_vers >= 12.0 verified=false external=false rentable=true',
            sort_order='dph-, dlperf'
        )
    except ValueError as e:
        logger.error(f"Search offers error: {e}",)
        raise e

    return offers


def create_instance(offer, c):
    try:
        res = client.create_instance(id=offer.id, image="nvidia/cuda:12.0.1-devel-ubuntu20.04", ssh=True,
                                     env=f"-e ETH_ADDRESS={eth_address} -e CUDA_COMPUTE={c['cuda_compute']} -e GPU_NUMS={c['gpu_nums']}",
                                     onstart="onstart.sh")
    except Exception as e:
        logger.error(f"Error: {e}")
        return False
    if not res['success']:
        logger.error(f"Create Instance error: {res}")
        return False
    return True


def rob_it(c):
    limit = c['machine_nums']

    offers = search_offers(c)
    while limit > 0:
        if not offers:
            logger.info("not available offers, sleep 5 seconds")
            time.sleep(5)
        for offer in offers:
            if create_instance(offer, c):
                limit -= 1
                logger.success(f"Create instance success {offer.id}")
            else:
                logger.error(f"Create instance failed {offer.id}")

            if limit == 0:
                break

processes = []
logger.info(f"config: {machine_configs}")
for cfg in machine_configs:
    thread = Thread(target=rob_it, args=(cfg,))
    logger.info(f"start thread {thread.ident}")
    thread.start()
    processes.append(thread)

# wait thread finish
for process in processes:
    process.join()

print("program done!!!")