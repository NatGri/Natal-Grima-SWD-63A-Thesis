from appGUI import Nutrition

if __name__ == '__main__':
    try:
        system = Nutrition()
        system.start()
    except Exception as e:
        print(e.with_traceback())
    except KeyboardInterrupt:
        print('Exited Normally')
