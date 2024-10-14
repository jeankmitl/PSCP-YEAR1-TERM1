"""SaveComputeRepeat"""
def main():
    """SaveComputeRepeat"""
    start_here = 492137954293754252786

    miliseconds = start_here
    seconds = miliseconds//1000
    miliseconds = miliseconds%1000
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24

    print(days, hours, minutes, seconds, miliseconds)
main()
