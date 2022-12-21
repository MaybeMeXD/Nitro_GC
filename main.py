import threading,ctypes,string,os,time,requests,numpy
from pystyle import Colors, Colorate
from discord_webhook import DiscordWebhook

USE_WEBHOOK = True


time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

class NitroGen: 
    def __init__(self): 
        self.fileName = "NitroC.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro G-C ProxyLess By @MaybeMeXD")  
        else:  
            print(f'\33]0;Nitro Generator and Checker \a',
                  end='', flush=True) 

        print(Colorate.Horizontal(Colors.blue_to_red, """  _   _ _ _                _____         _____ 
 | \ | (_) |              / ____|       / ____|
 |  \| |_| |_ _ __ ___   | |  __ ______| |     
 | . ` | | __| '__/ _ \  | | |_ |______| |     
 | |\  | | |_| | | (_) | | |__| |      | |____ 
 |_| \_|_|\__|_|  \___/   \_____|       \_____|
                                               
                                               """, 3)) 
        self.slowType(
            "\nInput How Many Codes to Generate and Check: ", .00, newLine=False)
            

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore: ", .00, newLine=False)
            url = input('') 
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook( 
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                        
                    ).execute()
        valid = [] 
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}" 
                result = self.quickChecker(url, webhook)  
                if result:  
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
               
                print("\nInterrupted by user")
                break 
            except Exception as e:  
                print(f" Error | {url} ")  

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro G-C - {len(valid)} Valid | {invalid} Invalid - ")  # Change the title
                print("")
            else:  
                print(
                    f'\33]0;Nitro G-C - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268 UPDATED BY https://github.com/MaybeMeXD\a', end='', flush=True)

        print(f"""
Results:

 Valid: {len(valid)}
 Invalid: {invalid}""")
        input("\nCheck Finish ! Press Enter to close the program.")
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text: 
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  
    def quickChecker(self, nitro:str, notify=None):  

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 
        if response.status_code == 200:  

            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w", encoding="utf8") as file: 

                file.write(nitro)
            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"BRO WTF GOT A NITRO IN A NITRO GEN !! @everyone \n{nitro}"
                ).execute()
            return True 
        else:
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False 
if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main() 