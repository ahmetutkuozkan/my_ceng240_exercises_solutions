def buy_hats(hats_cost,money):
    max_hat_number=0
    hats_cost.sort()
    for i in hats_cost:
        if(money>=i):
            money-=i
            max_hat_number+=1
        else:
            break
    return max_hat_number