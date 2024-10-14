'''pinger'''
def main():
    '''pinger'''
    web1 = input().rstrip()
    useless2 = input().rstrip()
    web1 = web1 * 1
    useless2 = useless2*1
    pinging3 = input().rstrip()
    reps = [input().rstrip() for _ in range(4)]
    address = ''
    if pinging3.find('[') != -1:
        address += pinging3[pinging3.find('[') + 1:pinging3.find(']')]
    else:
        address += pinging3[pinging3.find('Pinging') + 8:pinging3.find('with') - 1]
    received = 0
    lost = 0
    highest = 0
    lowest = float('inf')
    total_ms = 0
    for i in reps:
        if i in ['Request timed out.', 'General failure.']:
            lost += 1
        elif 'time=' in i:
            packetlocation = i[i.find('time=') + 5:i.find('ms')]
            received += 1
            packetlocation = int(packetlocation)
            if packetlocation < lowest:
                lowest = packetlocation
            if packetlocation > highest:
                highest = packetlocation
            total_ms += packetlocation
        else:
            received += 1
    if lowest == float('inf'):
        lowest = 0
    # avg
    loss = 100
    avg_ms = 0
    if received > 0:
        avg_ms = total_ms // received
        loss = 100 * (lost / 4)
    print(f'Ping statistics for {address}:')
    print(f'    Packets: Sent = 4, Received = {received}, Lost = {lost} ({loss:.0f}% loss),')
    if lost < 4:
        print('Approximate round trip times in milli-seconds:')
        print(f'    Minimum = {lowest}ms, Maximum = {highest}ms, Average = {avg_ms}ms')
main()
