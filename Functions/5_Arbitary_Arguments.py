def non_key_keyword_args(*args,**kwargs):
    for i in args:
        print(i,end=" ")

# for printing keywords arguments
    print()
    for key,val in kwargs.items():
        print(f'{key} : {val}')


non_key_keyword_args('Hello','How','What','When','Where',Name='Sahil',job='Engineer',salary=50_000)
