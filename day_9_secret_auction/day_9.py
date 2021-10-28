# secret auction
auction_log = []
bids = []
running = True
def game():
    name = input('enter your name: ')
    bid = int(input('enter your bid: $'))
    finish = input('continue? (yes/no): ')

    def auction(name_log, bid_log, finish_log):
        global auction_log
        global running
        new_bidder = {}
        new_bidder['name'] = name_log
        new_bidder['bid'] = bid_log
        new_bidder['finish'] = finish_log
        auction_log.append(new_bidder)
        if finish_log == 'no':
            running = False

    auction(name, bid, finish)


while running:
    print('\n\n\n\n\n\n\n\n\n\n\n')
    game()



if not running:
    print('\n\n\n\n\n\n\n\n\n\n\n')
    for bidders in auction_log:
        bids.append(bidders['bid'])
    for bidders in auction_log:
        if bidders['bid'] == max(bids):
            print(f"{bidders['name']} made the highest bid with ${max(bids)}.")
