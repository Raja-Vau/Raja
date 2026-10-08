from Kamal import approval_system, BNG_71_
import time

if __name__ == "__main__":
    approval_system()
    try:
        BNG_71_()
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
