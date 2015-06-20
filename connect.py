__author__ = 'ColemanTung'


import pylibmc

mc = pylibmc.Client(["127.0.0.1"])

mc["foo"] = "ABCDEFG"
print(mc.get("foo"))

#(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "verify_keys": True, "ketama": True})