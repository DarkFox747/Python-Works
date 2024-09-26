mylist = ['892a10085a7ffff', '892a10085b7ffff', '892a1008803ffff',
       '892a1008807ffff', '892a100880bffff', '892a100880fffff',
       '892a1008813ffff', '892a1008817ffff', '892a100881bffff',
       '892a1008823ffff', '892a1008827ffff', '892a100882bffff',
       '892a100882fffff', '892a1008833ffff', '892a1008837ffff',
       '892a100883bffff', '892a1008867ffff', '892a1008877ffff',
       '892a1008883ffff', '892a1008887ffff', '892a100888bffff',
       '892a100888fffff', '892a1008893ffff', '892a1008897ffff',
       '892a100889bffff', '892a10088a3ffff', '892a10088a7ffff',
       '892a10088abffff', '892a10088afffff', '892a10088b3ffff',
       '892a10088b7ffff', '892a10088bbffff', '892a10088c3ffff',
       '892a10088d7ffff', '892a1008903ffff', '892a1008907ffff',
       '892a100890bffff', '892a100890fffff', '892a1008913ffff',
       '892a1008917ffff', '892a100891bffff', '892a1008923ffff',
       '892a1008927ffff', '892a100892bffff', '892a100892fffff',
       '892a1008933ffff', '892a1008937ffff', '892a100893bffff',
       '892a1008943ffff', '892a1008947ffff', '892a100894bffff',
       '892a100894fffff', '892a1008953ffff', '892a1008957ffff',
       '892a100895bffff', '892a1008963ffff', '892a1008967ffff',
       '892a100896bffff', '892a100896fffff', '892a1008973ffff',
       '892a1008977ffff', '892a100897bffff', '892a1008983ffff',
       '892a1008987ffff', '892a100898bffff', '892a100898fffff',
       '892a1008993ffff', '892a1008997ffff', '892a100899bffff',
       '892a10089a3ffff', '892a10089a7ffff', '892a10089abffff',
       '892a10089afffff', '892a10089b3ffff', '892a10089b7ffff']

a = ','.join("'{0}'".format(x) for x in mylist)
b= "'hhi_020t034','hhi_035t049','hhi_050t099','hhi_200plus'"
c= a+","+b
print(c)