from Path import bank_API #all non specified functions here



def business_model(business, card_inp, pin, account):
    '''
    intakes str determining whether the user want to 'See Balance', 'Deposit', or 'Withdraw'
    '''
    if business == 'See Balance' and bank_API.valid_access_check(card_inp,pin):
        return bank_API.balance(account)
    elif business == 'Deposit' and bank_API.valid_access_check(card_inp,pin):
        deposit_amount = input('please deposit cash now') #automatically calculated from the machine
        return bank_API.balance(account) + deposit_amount
    else:
        withdraw_amount = input('please enter the amount you wish to withdraw') 
        return bank_API.balance(account) - withdraw_amount

def inactivity_timer(): 
    '''
    returns a boolean on whether or not the inactivity timer has run out of time yet (~45 sec)
    possibly built into bank_API
    '''
    pass

def atm_process():
    '''
    main code block to run the cascade
    '''
    card_inp = input('please insert card') #
    if bank_API.valid_card(card_inp):
        while(inactivity_timer()):
            pin = input('please apply your pin number')
            if bank_API.valid_access_check(card_inp, pin):
                print(bank_API.available_accounts(card_inp, pin))
                account = input('please select your account')
                business = input('please select one of the following options: See Balance/Deposit/Withdraw')
                print(business_model(business,card_inp,pin,account))
            else:
                print('please try again')
        


