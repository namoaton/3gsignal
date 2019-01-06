import spur
import ttk
import Tkinter
import ttk
import thread
from time import sleep
import datetime
ip_hostname ="192.168.1.1"
user = "user"
passw = "password"
def get_rssi():
    shell = spur.SshShell(hostname=ip_hostname, username=user, password=passw,load_system_host_keys="False",missing_host_key =spur.ssh.MissingHostKey.accept)
    spur.ssh.MissingHostKey.accept
    try: 
        result = shell.run(["comgt", "sig" ,"-d", "/dev/ttyUSB1"])
        result_string  = result.output
    except result.to_error():
        return 0
    if result_string[0] == 'S': 
        signal_str_val = result_string[16:20]
        try:
            signal_in_percent = (float(signal_str_val.replace(',','.'))/31.0)*100
        # value.set("3g signal strength"+" %.2g" %(signal_in_percent)+"%")
        # pb["value"]= signal_in_percent
            print " %.2g" %(signal_in_percent)+"%"
            return signal_in_percent
        except ValueError:
            pass
    return 0
def get_ip():
    shell = spur.SshShell(hostname=ip_hostname, username=user, password=passw,load_system_host_keys="False",missing_host_key =spur.ssh.MissingHostKey.accept)
    spur.ssh.MissingHostKey.accept
    result_ip_string ="0.0.0.0"
    try: 
        result_ip = shell.run(["wget", "-qO-",'http://ipecho.net/plain'])
        result_ip_string = result_ip.output       
    # except result.to_error():
    #     return "None"
    except ValueError:
         return "None"
    return result_ip_string
    
top = Tkinter.Tk()
top.geometry('210x100')
top.title('3g signal strength')
value =Tkinter.StringVar()
modem_label =Tkinter.Label(top,textvariable = value)
modem_label.pack()
pb = ttk.Progressbar(top,orient ="horizontal",length = 200, mode ="determinate", value=20, maximum=100)
pb.pack()
time_value = Tkinter.StringVar()
time_label = Tkinter.Label(top, textvariable = time_value)
time_label.pack()
ip_label_value = Tkinter.StringVar()
ip_label = Tkinter.Label(top,textvariable = ip_label_value,text="Helvetica", font=("Helvetica", 16))
ip_label.pack()
signal_in_percent = 0
def update_progress_bar():
    signal_val = get_rssi()
    if signal_val > 0:
        signal_in_percent = signal_val
    try:
        value.set("3g signal strength"+" %.2g" %(signal_in_percent)+"%")
        pb["value"]= signal_in_percent
        ip = get_ip()
        ip_label_value.set(ip)
    except UnboundLocalError:
        print "error"
    top.after(30000, update_progress_bar)
def update_time():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    time_value.set(time)
    top.after(1000, update_time)
top.after(0, update_progress_bar)
top.after(0, update_time)
top.mainloop()
