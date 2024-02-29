import psutil
import platform
import GPUtil
from flask import Flask, jsonify

app = Flask(__name__)

def get_hardware_specs():
    specs = {}

    # CPU information
    specs['cpu'] = {
        'brand': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'threads': psutil.cpu_count(logical=True)
    }

    # Memory information
    memory = psutil.virtual_memory()
    specs['memory'] = {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'free': memory.free
    }

    # Disk information
    disk = psutil.disk_usage('/')
    specs['disk'] = {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free
    }

    # GPU information
    gpus = GPUtil.getGPUs()
    if gpus:
        specs['gpu'] = []
        for gpu in gpus:
            specs['gpu'].append({
                'name': gpu.name,
                'memory_total': gpu.memoryTotal,
                'memory_used': gpu.memoryUsed,
                'memory_free': gpu.memoryFree,
                'temperature': gpu.temperature,
                'load': gpu.load
            })

    return specs

@app.route('/hardware_specs', methods=['GET'])
def hardware_specs():
    specs = get_hardware_specs()
    return jsonify(specs)

if __name__ == '__main__':
    app.run(debug=True)


#Run on command line:
#    curl http://127.0.0.1:5000/hardware_specs
#    {
#  "cpu": {
#    "brand": "x86_64",
#    "cores": 4,
#    "threads": 4
#  },
#  "disk": {
#    "free": 73857335296,
#    "total": 234621349888,
#    "used": 148771348480
#  },
#  "memory": {
#    "available": 3520290816,
#    "free": 851931136,
#    "total": 8192471040,
#    "used": 3663450112
#  }
#}

