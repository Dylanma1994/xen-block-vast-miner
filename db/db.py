import sqlite3

DATABASE_NAME = 'vast.sqlite'

def init_db():
    conn = sqlite3.connect(database=DATABASE_NAME)
    conn.execute('''
CREATE TABLE IF NOT EXISTS instances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    actual_status TEXT,
    bundle_id INTEGER,
    bw_nvlink REAL,
    compute_cap INTEGER,
    cpu_cores INTEGER,
    cpu_cores_effective REAL,
    cpu_name TEXT,
    cpu_ram INTEGER,
    cpu_util REAL,
    cuda_max_good REAL,
    cur_state TEXT,
    direct_port_count INTEGER,
    direct_port_end INTEGER,
    direct_port_start INTEGER,
    disk_bw REAL,
    disk_name TEXT,
    disk_space REAL,
    disk_util REAL,
    dlperf REAL,
    dlperf_per_dphtotal REAL,
    dph_base REAL,
    dph_total REAL,
    driver_version TEXT,
    duration REAL,
    end_date TEXT,
    external INTEGER,
    flops_per_dphtotal REAL,
    geolocation TEXT,
    gpu_display_active INTEGER,
    gpu_frac REAL,
    gpu_lanes INTEGER,
    gpu_mem_bw REAL,
    gpu_name TEXT,
    gpu_ram INTEGER,
    gpu_temp REAL,
    gpu_util REAL,
    has_avx INTEGER,
    host_id INTEGER,
    hosting_type INTEGER,
    image_args TEXT,
    image_runtype TEXT,
    image_uuid TEXT,
    inet_down REAL,
    inet_down_billed REAL,
    inet_down_cost REAL,
    inet_up REAL,
    inet_up_billed REAL,
    inet_up_cost REAL,
    intended_status TEXT,
    is_bid INTEGER,
    jupyter_token TEXT,
    label TEXT,
    local_ipaddrs TEXT,
    logo TEXT,
    machine_dir_ssh_port INTEGER,
    machine_id INTEGER,
    mem_limit REAL,
    mem_usage REAL,
    min_bid REAL,
    mobo_name TEXT,
    next_state TEXT,
    num_gpus INTEGER,
    pci_gen REAL,
    pcie_bw REAL,
    ports BLOB,
    public_ipaddr TEXT,
    reliability2 REAL,
    rentable INTEGER,
    score REAL,
    ssh_host TEXT,
    ssh_idx TEXT,
    ssh_port INTEGER,
    start_date REAL,
    status_msg TEXT,
    storage_cost REAL,
    storage_total_cost REAL,
    total_flops REAL,
    verification TEXT,
    vmem_usage REAL,
    webpage TEXT
    )
'''
    )
    conn.commit()
    conn.close()


def insert(row_data: dict):
    insert_query = '''
    INSERT INTO instances (
        actual_status, bundle_id, bw_nvlink, compute_cap, cpu_cores, cpu_cores_effective,
        cpu_name, cpu_ram, cpu_util, cuda_max_good, cur_state, direct_port_count,
        direct_port_end, direct_port_start, disk_bw, disk_name, disk_space, disk_util,
        dlperf, dlperf_per_dphtotal, dph_base, dph_total, driver_version, duration,
        end_date, external, flops_per_dphtotal, geolocation, gpu_display_active,
        gpu_frac, gpu_lanes, gpu_mem_bw, gpu_name, gpu_ram, gpu_temp, gpu_util,
        has_avx, host_id, hosting_type, image_args, image_runtype, image_uuid,
        inet_down, inet_down_billed, inet_down_cost, inet_up, inet_up_billed,
        inet_up_cost, intended_status, is_bid, jupyter_token, label, local_ipaddrs,
        logo, machine_dir_ssh_port, machine_id, mem_limit, mem_usage, min_bid,
        mobo_name, next_state, num_gpus, pci_gen, pcie_bw, ports, public_ipaddr,
        reliability2, rentable, score, ssh_host, ssh_idx, ssh_port, start_date,
        status_msg, storage_cost, storage_total_cost, total_flops, verification,
        vmem_usage, webpage
    ) VALUES (
        :actual_status, :bundle_id, :bw_nvlink, :compute_cap, :cpu_cores, :cpu_cores_effective,
        :cpu_name, :cpu_ram, :cpu_util, :cuda_max_good, :cur_state, :direct_port_count,
        :direct_port_end, :direct_port_start, :disk_bw, :disk_name, :disk_space, :disk_util,
        :dlperf, :dlperf_per_dphtotal, :dph_base, :dph_total, :driver_version, :duration,
        :end_date, :external, :flops_per_dphtotal, :geolocation, :gpu_display_active,
        :gpu_frac, :gpu_lanes, :gpu_mem_bw, :gpu_name, :gpu_ram, :gpu_temp, :gpu_util,
        :has_avx, :host_id, :hosting_type, :image_args, :image_runtype, :image_uuid,
        :inet_down, :inet_down_billed, :inet_down_cost, :inet_up, :inet_up_billed,
        :inet_up_cost, :intended_status, :is_bid, :jupyter_token, :label, :local_ipaddrs,
        :logo, :machine_dir_ssh_port, :machine_id, :mem_limit, :mem_usage, :min_bid,
        :mobo_name, :next_state, :num_gpus, :pci_gen, :pcie_bw, :ports, :public_ipaddr,
        :reliability2, :rentable, :score, :ssh_host, :ssh_idx, :ssh_port, :start_date,
        :status_msg, :storage_cost, :storage_total_cost, :total_flops, :verification,
        :vmem_usage, :webpage
    )
    '''
    with sqlite3.connect(database=DATABASE_NAME) as conn:
        conn.execute(insert_query, row_data)
        conn.commit()


init_db()
print("init success")