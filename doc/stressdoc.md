## Stress testing sorting algorithms

A tesztelés során három algoritmust teszteltünk:

- Bubble sort
- Coctail Shaker sort
- Merge sort

Mind lebegőpontos és egész számokra teszteltük az algoritmusokat.
A tömbjeink nagysága 50, 250, 500, 1000, 5000, 7500.

Jól látható, hogy a rendezések gyorsasága a Bubble  és a Coctail Shaker sort esetében
exponenciálisan növekednek az egyre nagyobb tömbméretek következtében.


###A Bubble sort algoritmus eredménye:

- Int 50 element array test: 0.0009822845458984375sec
- Float 50 element array test: 0.0009992122650146484sec
- Int 250 element array test: 0.02194380760192871sec
- Float 250 element array test: 0.022230148315429688sec
- Int 500 element array test: 0.08161568641662598sec
- Float 500 element array test: 0.06981492042541504sec
- Int 1000 element array test: 0.27841806411743164sec
- Float 1000 element array test: 0.2148139476776123sec
- Int 5000 element array test: 6.755751609802246sec
- Float 5000 element array test: 6.538065433502197sec
- Int 7500 element array test: 16.40373158454895sec
- Float 7500 element array test: 15.649327754974365sec

###A Coctail Shaker sort eredménye:

- Int 50 element array test: 0.0009965896606445312sec
- Float 50 element array test: 0.0010292530059814453sec
- Int 250 element array test: 0.016918182373046875sec
- Float 250 element array test: 0.02352142333984375sec
- Int 500 element array test: 0.0718080997467041sec
- Float 500 element array test: 0.06881594657897949sec
- Int 1000 element array test: 0.30974555015563965sec
- Float 1000 element array test: 0.2949097156524658sec
- Int 5000 element array test: 7.354368209838867sec
- Float 5000 element array test: 7.962470531463623sec
- Int 7500 element array test: 17.602890491485596sec
- Float 7500 element array test: 17.335631370544434sec

###A Merge sort eredménye:

- Int 50 element array test: 0.0sec
- Float 50 element array test: 0.0sec
- Int 250 element array test: 0.0019943714141845703sec
- Float 250 element array test: 0.0019948482513427734sec
- Int 500 element array test: 0.002991914749145508sec
- Float 500 element array test: 0.003988981246948242sec
- Int 1000 element array test: 0.007024049758911133sec
- Float 1000 element array test: 0.006940364837646484sec
- Int 5000 element array test: 0.04583120346069336sec
- Float 5000 element array test: 0.05003976821899414sec
- Int 7500 element array test: 0.07623696327209473sec
- Float 7500 element array test: 0.06781506538391113sec
