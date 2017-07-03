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
        result_ip = shell.run(["wget", "-qO","- http://ipecho.net/plain", ";", "echo"])
        rusult_ip_string = result_ip.output       
    except result.to_error():
        return 0
    if result_string[0] == 'S': 
        signal_str_val = result_string[15:17]
        try:
            signal_in_percent = (int(signal_str_val)/31.0)*100
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
    try: 
        result_ip = shell.run(["wget", "-qO","- http://ipecho.net/plain", ";", "echo"])
        rusult_ip_string = result_ip.output       
    except result.to_error():
        return "None"
    except ValueError:
         return "None"
    return rusult_ip_string
    
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
ip_label = Tkinter.Label(top,textvariable = ip_label_value)
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
# class modem_rssi(Tkinter.Frame):
#     """docstring for modem_rssi"""
#     def __init__(self, master):
    	
#         Tkinter.Frame.__init__(self, master)
#         self.value =Tkinter.StringVar()
#         self.label = Tkinter.Label(self,textvariable = self.value)
#         self.label.pack()
#         self.pb = ttk.Progressbar(self,orient ="horizontal",length = 200, mode ="determinate", value=20, maximum=100)
#         self.pb.pack()
#         thread.start_new_thread(self.get_rssi())
#         # self.shell = spur.SshShell(hostname="192.168.1.1", username="root", password="aton",load_system_host_keys="False",missing_host_key =spur.ssh.MissingHostKey.accept) 
#         # self.result = self.shell.run(["comgt", "sig" ,"-d", "/dev/ttyUSB1"])
#         # self.result_string  = self.result.output
#         # if self.result_string[0] == 'S': 
#         #     self.signal_str_val = self.result_string[15:17]
#         #     self.signal_in_percent = (int(self.signal_str_val)/31.0)*100
#         #     self.value.set("3g signal strength"+" %.2g" %(self.signal_in_percent)+"%")
#         #     self.pb["value"]= self.signal_in_percent
#         #     print " %.2g" %(self.signal_in_percent)+"%"
#         #     sleep(0)
#     def get_rssi(self):
#             self.shell = spur.SshShell(hostname="192.168.1.1", username="root", password="aton",load_system_host_keys="False",missing_host_key =spur.ssh.MissingHostKey.accept) 
#             self.result = self.shell.run(["comgt", "sig" ,"-d", "/dev/ttyUSB1"])
#             self.result_string  = self.result.output
#             print self.result_string
#             if self.result_string[0] == 'S': 
#                 self.signal_str_val = self.result_string[15:17]
#                 self.signal_in_percent = (int(self.signal_str_val)/31.0)*100
#                 self.value.set("3g signal strength"+" %.2g" %(self.signal_in_percent)+"%")
#                 self.pb["value"]= self.signal_in_percent
#                 print " %.2g" %(self.signal_in_percent)+"%"
#             self.after(5000,self.get_rssi())
#                 # self.top.mainloop()
# root =Tkinter.Tk()
# root.geometry('210x100')
# root.title('3g signal strength')
# app = modem_rssi(root)
# root.mainloop()