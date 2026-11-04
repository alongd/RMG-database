# ruff: noqa: E501,F821
name = "O2VibrationalRelaxation"
shortDesc = "Sourced O2 heavy-particle V-T and V-V relaxation through v=10."
longDesc = """O2-O2 V-T/R and V-V from Annušová et al. (2018), Tables A2 and A3; O2-O V-T from Esposito et al. (2008), Eq. (3a-c), Tables 2-4. All entries are reversible; RMG derives reverse rates from loaded fixed-v thermo. O2-O2 bounds are 300-1000 K; O2-O bounds are the thermo-limited 100-5000 K domain (source valid 50-10000 K; absent 50-100 K and 5000-10000 K). O2-O2 V-V entries cover exactly high_v=2..10 with partner=0..high_v-2 and no identity exchanges. Tables use bounded, adaptively refined KineticsData with maximum 1% scanned source-formula interpolation error; values use cm^3/(molecule*s), converted by RMG. No O2(v=42) dissociation rates are included. Source PDF payloads remain in /home/alon/Data/vibkin, outside git."""

entry(
    index = 0,
    label = 'O2v1 + O2 <=> O2 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([7.521627413363876e-19, 1.2899246459573324e-18, 2.186427205379432e-18, 3.659547312599418e-18, 6.003241526790494e-18, 9.727943716084802e-18, 1.5568888320921682e-17, 2.460926185621176e-17, 3.84241521091412e-17, 5.955775051105684e-17, 9.117665922250602e-17, 1.3792047423521998e-16, 2.0703317108613136e-16, 3.0831208784879026e-16, 4.53882165268149e-16, 6.62999247192121e-16, 9.637655907019118e-16], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 1,
    label = 'O2v2 + O2 <=> O2v1 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([2.005916593299226e-18, 3.4168353941323195e-18, 5.75330251479151e-18, 9.567551590935736e-18, 1.5597686487359354e-17, 2.512251898013648e-17, 3.99701048962128e-17, 6.281734417843083e-17, 9.753389473089071e-17, 1.503486992899008e-16, 2.2894061245756763e-16, 3.44517255871342e-16, 5.145257392387545e-16, 7.624056548134136e-16, 1.1169399299074431e-15, 1.6238030396604805e-15, 2.349372388022447e-15], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 2,
    label = 'O2v3 + O2 <=> O2v2 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([4.164299822886286e-18, 7.042026367305777e-18, 1.1773449511412202e-17, 1.9443482370251418e-17, 3.148747228503496e-17, 5.038681129467083e-17, 7.965953819559688e-17, 1.2442382653622525e-16, 1.9203169036500676e-16, 2.9427481394718576e-16, 4.455381809046514e-16, 6.667327472954829e-16, 9.903108606889313e-16, 1.4595560959751077e-15, 2.1271693752419976e-15, 3.07672544984039e-15, 4.429134174176388e-15], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 3,
    label = 'O2v4 + O2 <=> O2v3 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([7.383130972158588e-18, 1.2374100605327671e-17, 2.050790814105371e-17, 3.3580265869062086e-17, 5.393678780202173e-17, 8.5622831374018e-17, 1.3431527434361635e-16, 2.0820708793828635e-16, 3.1897572080911485e-16, 4.852696740481308e-16, 7.295408810627762e-16, 1.0842697274288883e-15, 1.5996802571483309e-15, 2.3421563761126915e-15, 3.3916689979282418e-15, 4.874976115092748e-15, 6.974449611167641e-15], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 4,
    label = 'O2v5 + O2 <=> O2v4 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([1.226450472068644e-17, 2.0314239928041928e-17, 3.3281042220892777e-17, 5.388502664924345e-17, 8.561866568200333e-17, 1.344896217393474e-16, 2.0881344399801487e-16, 3.2046486095507927e-16, 4.861956351227039e-16, 7.326127274939141e-16, 1.091180648200153e-15, 1.6071402828292396e-15, 2.3501304782375827e-15, 3.411086143986915e-15, 4.89798629419307e-15, 6.981968261795013e-15, 9.90747002791181e-15], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 5,
    label = 'O2v6 + O2 <=> O2v5 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 328.5, 359.0, 391.5, 425.5, 461.5, 499.5, 539.5, 581.5, 626.0, 672.5, 721.0, 772.0, 825.5, 881.0, 939.0, 1000.0], 'K'),
        kdata = ([2.0941689408273153e-17, 3.414184484888766e-17, 5.5075339650244165e-17, 8.783407174619603e-17, 1.3754802415283907e-16, 2.130207434138837e-16, 3.26209987758342e-16, 4.939502924316332e-16, 7.396640476919949e-16, 1.1003013004187143e-15, 1.618473862285419e-15, 2.354980517043111e-15, 3.4028895441635263e-15, 4.8817156414357095e-15, 6.930554170361326e-15, 9.770080756303329e-15, 1.3712445360709311e-14], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*exp(((-2.16870e-3*v^3 + 1.02950e-2*v^2 - 9.03306e-2*v + 6.02557)*ln(T)) + (2.78130e-2*v^3 - 2.76608e-1*v^2 + 2.04169*v - 76.0376)); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 6,
    label = 'O2v7 + O2 <=> O2v6 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 327.5, 356.5, 387.5, 420.0, 454.5, 491.0, 530.0, 571.0, 614.0, 660.0, 708.5, 759.5, 814.0, 872.0, 1000.0], 'K'),
        kdata = ([3.313866670991786e-17, 5.3371250225979124e-17, 8.427586622942848e-17, 1.3149922708377431e-16, 2.0134208596519237e-16, 3.0464208918141893e-16, 4.554459414345382e-16, 6.761768518110583e-16, 9.917359211796018e-16, 1.4379613018385845e-15, 2.0788731710714e-15, 2.9839614737019134e-15, 4.254582231452239e-15, 6.068296362062255e-15, 8.656264156540179e-15, 1.77846547558789e-14], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*(2.44106e-33*T^6.25015)*exp((1.76911e-7*T^2 - 4.82968e-4*T + 5.40946e-1)*v); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 7,
    label = 'O2v8 + O2 <=> O2v7 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 327.0, 356.0, 386.5, 419.0, 453.5, 490.0, 528.5, 569.5, 612.5, 658.0, 706.0, 757.5, 812.0, 870.0, 1000.0], 'K'),
        kdata = ([5.0032778925515735e-17, 7.911798504016736e-17, 1.2371777933924372e-16, 1.8980157986047324e-16, 2.877491765428723e-16, 4.3092368508444676e-16, 6.374453572116801e-16, 9.316490858496198e-16, 1.3518674676244293e-15, 1.9391094036670954e-15, 2.7624106967170253e-15, 3.909387602670146e-15, 5.535218095214551e-15, 7.813538313188338e-15, 1.1034716960990572e-14, 2.249346883598141e-14], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*(2.44106e-33*T^6.25015)*exp((1.76911e-7*T^2 - 4.82968e-4*T + 5.40946e-1)*v); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 8,
    label = 'O2v9 + O2 <=> O2v8 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 327.0, 355.5, 386.0, 418.0, 452.0, 488.5, 527.0, 567.5, 610.0, 655.5, 703.5, 755.0, 809.5, 868.0, 1000.0], 'K'),
        kdata = ([7.553951970736171e-17, 1.182584637865691e-16, 1.8168162524364435e-16, 2.759315975764004e-16, 4.1150026032394e-16, 6.066094003639151e-16, 8.882535492527753e-16, 1.2847272727586418e-15, 1.836469144647798e-15, 2.596498392568285e-15, 3.660864381450678e-15, 5.127482881389161e-15, 7.18450017201717e-15, 1.0038410123061006e-14, 1.4076241904996422e-14, 2.844902795248347e-14], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*(2.44106e-33*T^6.25015)*exp((1.76911e-7*T^2 - 4.82968e-4*T + 5.40946e-1)*v); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 9,
    label = 'O2v10 + O2 <=> O2v9 + O2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 327.0, 355.5, 385.5, 417.5, 451.0, 487.0, 525.0, 565.5, 608.0, 653.0, 701.0, 752.5, 866.0, 1000.0], 'K'),
        kdata = ([1.1404961227745893e-16, 1.767621388494564e-16, 2.6877235995238056e-16, 4.0128162678896144e-16, 5.922807069251598e-16, 8.592520231417436e-16, 1.2388322904166e-15, 1.765217532865343e-15, 2.4974405541972627e-15, 3.4943651491898064e-15, 4.857281973352382e-15, 6.732592261073666e-15, 9.33481976784609e-15, 1.796837694746684e-14, 3.598143075853748e-14], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A2',
    longDesc = 'Source fit 0.25*(2.44106e-33*T^6.25015)*exp((1.76911e-7*T^2 - 4.82968e-4*T + 5.40946e-1)*v); V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).',
)

entry(
    index = 10,
    label = 'O2v1 + O2v1 <=> O2 + O2v2',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.7294020932172277e-14, 5.938386383778666e-14, 7.366241587450813e-14, 9.026873395804957e-14, 1.0945529837455305e-13, 1.316119286049255e-13, 1.567740491758161e-13, 1.853528015614552e-13, 2.1765277086770404e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=2), k=1.5*A*T^B; source A=2.2802e-17, B=1.2679. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 11,
    label = 'O2v1 + O2v2 <=> O2 + O2v3',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([5.81593807149617e-14, 7.357554167946034e-14, 9.191547753530883e-14, 1.133923770055745e-13, 1.3836813597494863e-13, 1.673892639005227e-13, 2.005420244657102e-13, 2.3840877045367534e-13, 2.8143737945962715e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=3), k=1.5*A*T^B; source A=2.2105e-17, B=1.3096. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 12,
    label = 'O2v2 + O2v2 <=> O2v1 + O2v3',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([1.5411998902568195e-13, 1.9015300845229636e-13, 2.31990364592339e-13, 2.798710070723784e-13, 3.3435495095606187e-13, 3.9636672960285413e-13, 4.658235513025571e-13, 6.305676365863544e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=3), k=1.5*A*T^B; source A=1.2973e-16, B=1.1702. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 13,
    label = 'O2v1 + O2v3 <=> O2 + O2v4',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.749224609819186e-14, 8.656149093386415e-14, 1.0955157322514671e-13, 1.3681509459909866e-13, 1.689000324470908e-13, 2.0660714406381117e-13, 2.501505146059501e-13, 3.0040034799702255e-13, 3.5806660817764074e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=4), k=1.5*A*T^B; source A=1.6591e-17, B=1.386. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 14,
    label = 'O2v2 + O2v3 <=> O2v1 + O2v4',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.836976341398126e-13, 2.2934339014768654e-13, 2.8295458239323367e-13, 3.449798288700911e-13, 4.162879959622465e-13, 4.982466852455165e-13, 5.909050818892208e-13, 6.956947090627691e-13, 8.136431641683775e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=4), k=1.5*A*T^B; source A=1.0618e-16, B=1.2361. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 15,
    label = 'O2v3 + O2v3 <=> O2v2 + O2v4',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([3.9765678542812664e-13, 4.802485049159059e-13, 5.741727520639862e-13, 6.795742317690234e-13, 7.973049425450299e-13, 9.28952721165074e-13, 1.0739419104456635e-12, 1.4096336116401989e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=4), k=1.5*A*T^B; source A=6.6026e-16, B=1.0511. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 16,
    label = 'O2v1 + O2v4 <=> O2 + O2v5',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([7.130570909410106e-14, 9.290878716040295e-14, 1.1935635061589157e-13, 1.5117810236064716e-13, 1.891445619410717e-13, 2.343505661819366e-13, 2.8720730002173036e-13, 3.4893301463854353e-13, 4.2057898985914756e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=5), k=1.5*A*T^B; source A=1.0611e-17, B=1.474. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 17,
    label = 'O2v2 + O2v4 <=> O2v1 + O2v5',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.9777744197516568e-13, 2.511649748092147e-13, 3.1491524530832423e-13, 3.8983345418266163e-13, 4.772479169867342e-13, 5.791443204768973e-13, 6.959002495044561e-13, 8.296430884759363e-13, 9.820381634940823e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=5), k=1.5*A*T^B; source A=6.6533e-17, B=1.331. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 18,
    label = 'O2v3 + O2v4 <=> O2v2 + O2v5',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([4.752083331998495e-13, 5.772864917040317e-13, 6.940350119390774e-13, 8.257580169110652e-13, 9.73641366993859e-13, 1.139811237427986e-12, 1.323669804966204e-12, 1.7521852976770997e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=5), k=1.5*A*T^B; source A=6.5477e-16, B=1.0838. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 19,
    label = 'O2v4 + O2v4 <=> O2v3 + O2v5',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([6.770458876693625e-13, 8.173867238788572e-13, 9.769310365111073e-13, 1.1559150623078533e-12, 1.3557763359218519e-12, 1.5792003565635903e-12, 1.825200401432355e-12, 2.3945421388570957e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=5), k=1.5*A*T^B; source A=1.1364e-15, B=1.0492. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 20,
    label = 'O2v1 + O2v5 <=> O2 + O2v6',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([7.359576361454077e-14, 9.711587133076978e-14, 1.2626692175045678e-13, 1.6175184667241875e-13, 2.04557224230398e-13, 2.5606182405169656e-13, 3.1688742673825165e-13, 3.885984946507973e-13, 4.725973975417869e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=6), k=1.5*A*T^B; source A=7.3215e-18, B=1.5446. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 21,
    label = 'O2v2 + O2v5 <=> O2v1 + O2v6',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.9176664721266827e-13, 2.4961398466373406e-13, 3.203644703914016e-13, 4.05413066651969e-13, 5.067958294317263e-13, 6.274102095779005e-13, 7.683258916488397e-13, 9.327620081078952e-13, 1.123487448330091e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=6), k=1.5*A*T^B; source A=2.9463e-17, B=1.4684. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 22,
    label = 'O2v3 + O2v5 <=> O2v2 + O2v6',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.88390888597975e-13, 6.072350545685623e-13, 7.46259410399495e-13, 9.0649448259473e-13, 1.0900515160373182e-12, 1.3003051255548077e-12, 1.5372351490749884e-12, 1.8043551917679802e-12, 2.104126078652135e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=6), k=1.5*A*T^B; source A=3.2187e-16, B=1.2131. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 23,
    label = 'O2v4 + O2v5 <=> O2v3 + O2v6',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([7.339480088115659e-13, 8.981282473595511e-13, 1.0872385132525686e-12, 1.3020374192923014e-12, 1.5447203284950007e-12, 1.819061436936717e-12, 2.1243547898928488e-12, 2.841778065378767e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=6), k=1.5*A*T^B; source A=8.0223e-16, B=1.1244. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 24,
    label = 'O2v5 + O2v5 <=> O2v4 + O2v6',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([1.015547320679483e-12, 1.2307738662576226e-12, 1.47636595927296e-12, 1.7528560330115877e-12, 2.0626288057902148e-12, 2.4100248111585827e-12, 2.7936836823772313e-12, 3.6854807691885265e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=5, w=6), k=1.5*A*T^B; source A=1.5087e-15, B=1.0706. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 25,
    label = 'O2v1 + O2v6 <=> O2 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.840538650456431e-14, 9.205724290723479e-14, 1.2193591045068613e-13, 1.5896790488125495e-13, 2.0440757271129563e-13, 2.5997691819316337e-13, 3.266260061415952e-13, 4.0637024267196803e-13, 5.01108472662425e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=7), k=1.5*A*T^B; source A=3.6462e-18, B=1.654. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 26,
    label = 'O2v2 + O2v6 <=> O2v1 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.8499749286547991e-13, 2.4393153756776624e-13, 3.169202378558715e-13, 4.057048442161535e-13, 5.127337513897208e-13, 6.414316809667175e-13, 7.933282176198058e-13, 9.723046569479317e-13, 1.181832623447988e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=7), k=1.5*A*T^B; source A=1.8861e-17, B=1.5403. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 27,
    label = 'O2v3 + O2v6 <=> O2v2 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.840745127734969e-13, 6.094145769105894e-13, 7.5782320447524e-13, 9.308420137720104e-13, 1.1311995469847677e-12, 1.3630744210185508e-12, 1.6269469628117157e-12, 1.9272400420325073e-12, 2.2672750444061204e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=7), k=1.5*A*T^B; source A=2.1474e-16, B=1.2825. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 28,
    label = 'O2v4 + O2v6 <=> O2v3 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([7.089158031613301e-13, 8.859915241276309e-13, 1.0941784085356858e-12, 1.335269717374708e-12, 1.6126943619097373e-12, 1.9318296385698217e-12, 2.2929241939077476e-12, 2.7016143358816057e-12, 3.161970192114665e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=7), k=1.5*A*T^B; source A=3.9643e-16, B=1.2419. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 29,
    label = 'O2v5 + O2v6 <=> O2v4 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([1.0272289214222753e-12, 1.266028932366261e-12, 1.5430057573277635e-12, 1.859677745946778e-12, 2.2196855588775132e-12, 2.629069313408403e-12, 3.0872139975516423e-12, 4.1725607995669946e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=5, w=7), k=1.5*A*T^B; source A=8.9477e-16, B=1.1642. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 30,
    label = 'O2v6 + O2v6 <=> O2v5 + O2v7',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([1.2889593532923077e-12, 1.5790210438730272e-12, 1.9134829702821985e-12, 2.293760228219063e-12, 2.7238118267307253e-12, 3.2104046531370506e-12, 3.7523643556490956e-12, 5.027518111929868e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=6, w=7), k=1.5*A*T^B; source A=1.3607e-15, B=1.1305. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 31,
    label = 'O2v1 + O2v7 <=> O2 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.211199838854529e-14, 8.514340458432816e-14, 1.1476367821744461e-13, 1.5210163905527243e-13, 1.9865572517410624e-13, 2.564623620107142e-13, 3.2680892302208406e-13, 4.121504445190842e-13, 5.148925336692104e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=8), k=1.5*A*T^B; source A=1.843e-18, B=1.7567. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 32,
    label = 'O2v2 + O2v7 <=> O2v1 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.7046185485319726e-13, 2.28500555146735e-13, 3.0153976296182867e-13, 3.9173952051821193e-13, 5.020410237345847e-13, 6.364938245467442e-13, 7.972560175150697e-13, 9.890375721051625e-13, 1.2162353162200635e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=8), k=1.5*A*T^B; source A=1.0295e-17, B=1.6321. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 33,
    label = 'O2v3 + O2v7 <=> O2v2 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.708053658629902e-13, 5.999794905948896e-13, 7.547494989109845e-13, 9.372149135017624e-13, 1.1507601182568942e-12, 1.4004013739781595e-12, 1.6872337883141564e-12, 2.016658347092744e-12, 2.392967837589242e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=8), k=1.5*A*T^B; source A=1.4179e-16, B=1.3504. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 34,
    label = 'O2v4 + O2v7 <=> O2v3 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.974344125122026e-13, 8.825075553519354e-13, 1.1027309362336505e-12, 1.3606777923929716e-12, 1.6607082618947838e-12, 2.009402511575738e-12, 2.4078123547746535e-12, 2.862951809669393e-12, 3.3802211868232776e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=8), k=1.5*A*T^B; source A=2.6312e-16, B=1.3109. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 35,
    label = 'O2v5 + O2v7 <=> O2v4 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.0406200022845283e-12, 1.2914057993416196e-12, 1.5842392347466628e-12, 1.9211661760289442e-12, 2.306500965053518e-12, 2.7471912519513615e-12, 3.2430579856137598e-12, 3.801317771134791e-12, 4.426965612516994e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=5, w=8), k=1.5*A*T^B; source A=7.2814e-16, B=1.2026. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 36,
    label = 'O2v6 + O2v7 <=> O2v5 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.2945128353095816e-12, 1.6070340283923028e-12, 1.9720745793007337e-12, 2.392212803006523e-12, 2.8728565846501164e-12, 3.422702651517778e-12, 4.041558299115549e-12, 4.738460790084874e-12, 5.519678844405546e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=6, w=8), k=1.5*A*T^B; source A=8.9603e-16, B=1.2045. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 37,
    label = 'O2v7 + O2v7 <=> O2v6 + O2v8',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([1.9872270665538964e-12, 2.4104596523848397e-12, 2.893809166529986e-12, 3.43839973849312e-12, 4.049002680686618e-12, 4.734254314736852e-12, 5.491549987798913e-12, 7.253561480109594e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=7, w=8), k=1.5*A*T^B; source A=2.8725e-15, B=1.0754. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 38,
    label = 'O2v1 + O2v8 <=> O2 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([5.5657693745227713e-14, 7.782736897558656e-14, 1.0689466296546366e-13, 1.4420959411782228e-13, 1.9154425076411426e-13, 2.512936738027549e-13, 3.2515132069003756e-13, 4.160993018105648e-13, 5.271679219950027e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=9), k=1.5*A*T^B; source A=8.7833e-19, B=1.8674. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 39,
    label = 'O2v2 + O2v8 <=> O2v1 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.5471449269620883e-13, 2.1068668687077457e-13, 2.82211373534428e-13, 3.7182736187366906e-13, 4.829244717751488e-13, 6.201233991637841e-13, 7.862182968296984e-13, 9.867206484936466e-13, 1.226959285413469e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=9), k=1.5*A*T^B; source A=5.6629e-18, B=1.7199. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 40,
    label = 'O2v3 + O2v8 <=> O2v2 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.3119923245575214e-13, 5.61786734898772e-13, 7.216445207144802e-13, 9.139698270708304e-13, 1.143414831731551e-12, 1.416590737036612e-12, 1.735976741938477e-12, 2.1089282836332725e-12, 2.5417908401327906e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=9), k=1.5*A*T^B; source A=6.435e-17, B=1.4735. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 41,
    label = 'O2v4 + O2v8 <=> O2v3 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.67455263439392e-13, 8.532146466034506e-13, 1.0764507843230888e-12, 1.3403810333492864e-12, 1.6500964502360536e-12, 2.0130896139884837e-12, 2.431176863924206e-12, 2.912461456172826e-12, 3.4634676396222803e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=9), k=1.5*A*T^B; source A=1.8223e-16, B=1.3676. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 42,
    label = 'O2v5 + O2v8 <=> O2v4 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([9.981363253698858e-13, 1.2600375054353112e-12, 1.5709694933883256e-12, 1.934377620823337e-12, 2.3562128614398357e-12, 2.8455154572854114e-12, 3.4035460363078786e-12, 4.039909448154688e-12, 4.761917827432893e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=5, w=9), k=1.5*A*T^B; source A=4.0578e-16, B=1.2978. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 43,
    label = 'O2v6 + O2v8 <=> O2v5 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.25638394906992e-12, 1.5840831536922902e-12, 1.9726634567723823e-12, 2.426308496632373e-12, 2.9523224164363916e-12, 3.5618409872122933e-12, 4.256295037509328e-12, 5.0474956331515385e-12, 5.944379827525404e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=6, w=9), k=1.5*A*T^B; source A=5.3127e-16, B=1.2909. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 44,
    label = 'O2v7 + O2v8 <=> O2v6 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([2.064485258582947e-12, 2.527569873318816e-12, 3.061232369004477e-12, 3.667667146405526e-12, 4.353125130864561e-12, 5.128324001858392e-12, 5.991325692448399e-12, 8.02048642010418e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=7, w=9), k=1.5*A*T^B; source A=2.2208e-15, B=1.1272. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 45,
    label = 'O2v8 + O2v8 <=> O2v7 + O2v9',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([2.8079825075180246e-12, 3.3811579902231373e-12, 4.031106175633158e-12, 4.758494464919329e-12, 5.568880353154952e-12, 6.472844736070674e-12, 7.46609663539072e-12, 9.758088394119202e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=8, w=9), k=1.5*A*T^B; source A=5.1224e-15, B=1.0346. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 46,
    label = 'O2v1 + O2v9 <=> O2 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([4.885256550414688e-14, 6.968914512946735e-14, 9.75429620040478e-14, 1.339607550548067e-13, 1.8096447836330118e-13, 2.4128327749707937e-13, 3.17025978438917e-13, 4.117035326701371e-13, 5.289994995067946e-13], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=1, w=10), k=1.5*A*T^B; source A=4.0885e-19, B=1.9786. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 47,
    label = 'O2v2 + O2v9 <=> O2v1 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.3935805851149757e-13, 1.9347297141087812e-13, 2.6393183085871466e-13, 3.5378911387597723e-13, 4.670666549250072e-13, 6.092079957104408e-13, 7.839214735721989e-13, 9.97906109266497e-13, 1.2578843283313962e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=2, w=10), k=1.5*A*T^B; source A=2.7628e-18, B=1.8274. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 48,
    label = 'O2v3 + O2v9 <=> O2v2 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([3.8785963900000477e-13, 5.147627666064973e-13, 6.729274927794848e-13, 8.664754779354439e-13, 1.1011191248934863e-12, 1.3847930684944938e-12, 1.7213241203467287e-12, 2.1197968180433708e-12, 2.5884824137332254e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=3, w=10), k=1.5*A*T^B; source A=3.2148e-17, B=1.5766. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 49,
    label = 'O2v4 + O2v9 <=> O2v3 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([6.197479476667061e-13, 8.107780485612455e-13, 1.0455657241507587e-12, 1.3291117707595373e-12, 1.6685982898606925e-12, 2.0741714378501654e-12, 2.5498957759701074e-12, 3.107131161221979e-12, 3.755805897584063e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=4, w=10), k=1.5*A*T^B; source A=8.1117e-17, B=1.4965. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 50,
    label = 'O2v5 + O2v9 <=> O2v4 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([9.211708843344564e-13, 1.1872859053365645e-12, 1.5096589408349602e-12, 1.8936914914600163e-12, 2.3475796545257876e-12, 2.8831839995552565e-12, 3.504098963773516e-12, 4.2233080056451056e-12, 5.05160412388907e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=5, w=10), k=1.5*A*T^B; source A=1.9357e-16, B=1.4135. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 51,
    label = 'O2v6 + O2v9 <=> O2v5 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 881.0, 1000.0], 'K'),
        kdata = ([1.201164931119187e-12, 1.5365364939381184e-12, 1.9398430622155663e-12, 2.416975629257086e-12, 2.9772190076224402e-12, 3.634216679177059e-12, 4.391349171346682e-12, 5.2633869786023854e-12, 6.26225637188606e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=6, w=10), k=1.5*A*T^B; source A=3.2073e-16, B=1.3715. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 52,
    label = 'O2v7 + O2v9 <=> O2v6 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([2.13352461858798e-12, 2.6353185624843107e-12, 3.2185839396879085e-12, 3.886793871982862e-12, 4.647905043109785e-12, 5.5149868338024735e-12, 6.487035225032252e-12, 8.795580390125717e-12], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=7, w=10), k=1.5*A*T^B; source A=1.7325e-15, B=1.1765. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 53,
    label = 'O2v8 + O2v9 <=> O2v7 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([3.052610850608141e-12, 3.684574573229264e-12, 4.402862392301516e-12, 5.208510750113929e-12, 6.107964078075359e-12, 7.113279721910855e-12, 8.219990193193046e-12, 1.078073494607179e-11], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=8, w=10), k=1.5*A*T^B; source A=5.1589e-15, B=1.048. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 54,
    label = 'O2v9 + O2v9 <=> O2v8 + O2v10',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([300.0, 359.0, 425.5, 499.5, 581.5, 672.5, 772.0, 1000.0], 'K'),
        kdata = ([3.623622162050508e-12, 4.351319606854559e-12, 5.174287289951783e-12, 6.092989641139548e-12, 7.114079937618988e-12, 8.250494175686532e-12, 9.496455258091e-12, 1.2362696631157006e-11], 'cm^3/(molecule*s)'),
        Tmin = (300, 'K'), Tmax = (1000, 'K')),
    shortDesc = 'Annušová et al. (2018), Table A3',
    longDesc = 'A3 pair (v=9, w=10), k=1.5*A*T^B; source A=7.2131e-15, B=1.0193. Source direction O2(partner+1)+O2(high_v-1) -> O2(partner)+O2(high_v); reverse from fixed-v detailed balance; bounds 300–1000 K; v=42 dissociation is excluded.',
)

entry(
    index = 55,
    label = 'O2v1 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 196.0, 632.0, 1045.5, 1931.5, 3256.5, 5000.0], 'K'),
        kdata = ([3.835244348532521e-12, 3.816243707649261e-12, 4.271125356829074e-12, 4.625794801570304e-12, 5.189929832690152e-12, 5.794624329726943e-12, 6.387150434602152e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=1) + O -> O2(w=0) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 56,
    label = 'O2v2 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 140.5, 201.5, 651.0, 1011.0, 1478.5, 2034.5, 3327.5, 5000.0], 'K'),
        kdata = ([2.6861891748872444e-12, 2.6303067490723897e-12, 2.637309534483485e-12, 3.0181714038300444e-12, 3.2900796001346723e-12, 3.5850373944698294e-12, 3.8798736888016525e-12, 4.42897453694473e-12, 4.983013552894171e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=2) + O -> O2(w=1) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 57,
    label = 'O2v2 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 116.0, 134.5, 155.5, 179.5, 206.5, 237.0, 271.0, 309.5, 353.0, 401.5, 456.0, 516.5, 660.0, 838.0, 1055.0, 1322.5, 1652.0, 2059.0, 3178.0, 5000.0], 'K'),
        kdata = ([5.454056411182234e-13, 7.441139582497832e-13, 9.862405082902191e-13, 1.2681429133814516e-12, 1.5906625679595474e-12, 1.946152119296112e-12, 2.332177215774799e-12, 2.7389860519521014e-12, 3.167915202340958e-12, 3.6127069973675972e-12, 4.0620359695143216e-12, 4.5141227627713125e-12, 4.958554906589896e-12, 5.817534201922503e-12, 6.602544261429718e-12, 7.280379668949214e-12, 7.846729048472249e-12, 8.292847476411118e-12, 8.616552754534322e-12, 8.903492416423047e-12, 8.741160607358713e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=2) + O -> O2(w=0) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 58,
    label = 'O2v3 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 142.0, 204.5, 659.5, 1021.5, 1492.0, 2051.5, 3339.0, 5000.0], 'K'),
        kdata = ([2.1226877412245443e-12, 2.068338225496069e-12, 2.0744932351070346e-12, 2.4246193683216776e-12, 2.6776523206960647e-12, 2.9564919262979833e-12, 3.2390802271948475e-12, 3.769767538844471e-12, 4.315845716312123e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=3) + O -> O2(w=2) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 59,
    label = 'O2v3 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 116.0, 134.5, 155.5, 179.5, 206.5, 237.0, 271.0, 309.5, 401.5, 516.5, 660.0, 837.5, 1054.5, 1322.0, 2058.0, 3176.5, 5000.0], 'K'),
        kdata = ([7.830178315833166e-13, 9.576419459824196e-13, 1.1494214518066418e-12, 1.352769893229262e-12, 1.5666843908057296e-12, 1.7853760786804953e-12, 2.007398157107827e-12, 2.227719241253851e-12, 2.4478175647760006e-12, 2.875333650217352e-12, 3.2715241905777793e-12, 3.6277979440294547e-12, 3.9365306284634734e-12, 4.1934502441609145e-12, 4.401451086198045e-12, 4.675011173322395e-12, 4.773606603997237e-12, 4.714977893372579e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=3) + O -> O2(w=1) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 60,
    label = 'O2v3 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 118.0, 138.5, 162.5, 189.5, 220.0, 255.0, 294.5, 339.0, 445.5, 578.0, 742.0, 942.5, 1194.0, 1498.5, 1864.5, 2301.5, 3435.0, 5000.0], 'K'),
        kdata = ([6.126761561667368e-13, 7.537837974182791e-13, 9.062882797120187e-13, 1.0735029982132512e-12, 1.247783522350938e-12, 1.4287181459230707e-12, 1.618084057308951e-12, 1.8117019600412127e-12, 2.0083159063222567e-12, 2.4068604946602906e-12, 2.8010398904040585e-12, 3.185518913586769e-12, 3.5537342634733728e-12, 3.912826668471873e-12, 4.248780830625734e-12, 4.5603704548971545e-12, 4.847216279420336e-12, 5.3490555049839955e-12, 5.759567867332769e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=3) + O -> O2(w=0) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 61,
    label = 'O2v4 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 141.0, 203.0, 655.5, 1016.5, 1485.5, 2043.5, 3333.5, 5000.0], 'K'),
        kdata = ([1.7667896613522982e-12, 1.7180900623654624e-12, 1.723714715793015e-12, 2.0506325751462405e-12, 2.290798896585804e-12, 2.558168389415541e-12, 2.832075829713325e-12, 3.355570213380982e-12, 3.903127661367592e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=4) + O -> O2(w=3) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 62,
    label = 'O2v4 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 116.5, 135.0, 156.5, 180.5, 239.0, 313.0, 406.5, 523.5, 669.5, 850.0, 1345.0, 2093.5, 3221.5, 5000.0], 'K'),
        kdata = ([9.695531322581228e-13, 1.1081979624361073e-12, 1.2462484939059118e-12, 1.3874230378896153e-12, 1.5250001904212699e-12, 1.7945645705413295e-12, 2.045411814252594e-12, 2.2743988074370833e-12, 2.4780431698213946e-12, 2.6558067292683116e-12, 2.8070226175379885e-12, 3.0346288758608617e-12, 3.1741869236867398e-12, 3.238279292094858e-12, 3.2380055396216513e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=4) + O -> O2(w=2) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 63,
    label = 'O2v4 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 118.5, 139.5, 163.5, 191.0, 258.0, 343.0, 451.5, 586.5, 753.0, 956.5, 1211.5, 1519.0, 2326.5, 3456.5, 5000.0], 'K'),
        kdata = ([8.731560316030684e-13, 1.0000435365081097e-12, 1.127435065290707e-12, 1.2556740625785201e-12, 1.3845859088734929e-12, 1.6405459790545237e-12, 1.8872015126363127e-12, 2.1254045824942095e-12, 2.3493312345720657e-12, 2.558463838959877e-12, 2.7526184793599203e-12, 2.9373200967965164e-12, 3.106494948411517e-12, 3.4025746975363407e-12, 3.648392159482503e-12, 3.85086685228802e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=4) + O -> O2(w=1) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 64,
    label = 'O2v4 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 119.5, 141.5, 167.0, 196.5, 268.0, 359.5, 475.5, 619.0, 795.0, 1008.5, 1275.0, 1593.0, 2412.0, 3526.5, 5000.0], 'K'),
        kdata = ([7.59546491157147e-13, 8.743110409101346e-13, 9.894455548672392e-13, 1.1078049679454863e-12, 1.228825064292907e-12, 1.4713773315562774e-12, 1.7128398121874016e-12, 1.951235301061763e-12, 2.1818908230076113e-12, 2.4045720151621225e-12, 2.618620602740645e-12, 2.8309551601523426e-12, 3.033092313772052e-12, 3.4088336964834236e-12, 3.74947776934408e-12, 4.057743526688498e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=4) + O -> O2(w=0) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 65,
    label = 'O2v5 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 140.0, 200.0, 647.5, 1006.0, 1472.0, 2027.0, 3322.5, 5000.0], 'K'),
        kdata = ([1.5159191116082985e-12, 1.4731455501380708e-12, 1.478772754926036e-12, 1.7870984905123647e-12, 2.017022129621007e-12, 2.2753330511260225e-12, 2.5424667821947785e-12, 3.0632410372529884e-12, 3.6156922989173676e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=5) + O -> O2(w=4) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 66,
    label = 'O2v5 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 136.5, 184.0, 245.5, 323.5, 422.5, 546.0, 888.5, 1412.5, 2190.0, 5000.0], 'K'),
        kdata = ([1.1090104429563634e-12, 1.3004481213797963e-12, 1.4779935163121071e-12, 1.6404046059331965e-12, 1.7852779076657934e-12, 1.914254387159875e-12, 2.026893882017729e-12, 2.208989207532663e-12, 2.3433259486447215e-12, 2.436571632742355e-12, 2.5311300205380488e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=5) + O -> O2(w=3) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 67,
    label = 'O2v5 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 141.0, 195.0, 265.0, 354.5, 468.0, 609.0, 992.5, 1571.0, 2387.0, 3507.0, 5000.0], 'K'),
        kdata = ([1.1048292499902088e-12, 1.294488130243695e-12, 1.4723475411862026e-12, 1.6377683363449528e-12, 1.7909432696216982e-12, 1.932959379628962e-12, 2.063305616843252e-12, 2.292825545127262e-12, 2.493188890431452e-12, 2.6622400390264647e-12, 2.80635170371987e-12, 2.9296938358083207e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=5) + O -> O2(w=2) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 68,
    label = 'O2v5 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 120.0, 143.0, 200.5, 275.0, 369.5, 489.5, 638.5, 1039.5, 1634.5, 2457.5, 3562.0, 5000.0], 'K'),
        kdata = ([1.0304902183932044e-12, 1.124518191977159e-12, 1.2160441915711656e-12, 1.3946413359863249e-12, 1.5632367447049528e-12, 1.7214817905560009e-12, 1.8721863885145195e-12, 2.0142692796715712e-12, 2.273232854405118e-12, 2.511048540535772e-12, 2.722645549798099e-12, 2.9128092182785754e-12, 3.084436940823827e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=5) + O -> O2(w=1) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 69,
    label = 'O2v5 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 120.0, 143.5, 201.5, 277.0, 373.0, 494.5, 645.0, 828.5, 1049.5, 1647.5, 2471.5, 3572.5, 5000.0], 'K'),
        kdata = ([7.55285901903896e-13, 8.436226971614193e-13, 9.33546142997101e-13, 1.11229452655661e-12, 1.2883856664047435e-12, 1.4595519918084123e-12, 1.6268740999216715e-12, 1.7886170923112163e-12, 1.944286645481581e-12, 2.093954945949218e-12, 2.3858077135888627e-12, 2.654715358725139e-12, 2.9037250912348135e-12, 3.1345269798351658e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=5) + O -> O2(w=0) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 70,
    label = 'O2v6 + O <=> O2v5 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 139.0, 196.5, 637.5, 993.0, 1455.5, 2007.0, 2612.0, 3308.5, 5000.0], 'K'),
        kdata = ([1.3279810876992134e-12, 1.2907198717862257e-12, 1.2965302308211132e-12, 1.5889343612382752e-12, 1.810352969652918e-12, 2.0611337860608203e-12, 2.3226562035122407e-12, 2.5777425504771747e-12, 2.8425540286238037e-12, 3.4016268371499375e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=5) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 71,
    label = 'O2v6 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 141.0, 195.0, 265.0, 354.0, 608.0, 991.5, 1569.5, 2385.5, 5000.0], 'K'),
        kdata = ([1.2082160920071967e-12, 1.3263870315760399e-12, 1.4308233230333967e-12, 1.5233307214950146e-12, 1.6051794757556494e-12, 1.744429046047641e-12, 1.8560233746850214e-12, 1.9494766710781368e-12, 2.025873888219075e-12, 2.1425006254294446e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=4) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 72,
    label = 'O2v6 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 145.5, 206.5, 285.5, 386.0, 669.5, 1086.0, 1694.0, 2520.0, 5000.0], 'K'),
        kdata = ([1.2982163055487306e-12, 1.4175958020314075e-12, 1.5255832572712513e-12, 1.6228650442385092e-12, 1.7114353355878627e-12, 1.868932815969545e-12, 2.00359162156256e-12, 2.1249793467417987e-12, 2.2319146885113735e-12, 2.413996092010366e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=3) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 73,
    label = 'O2v6 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 147.5, 210.5, 292.5, 396.5, 688.5, 1114.5, 1729.0, 2555.5, 5000.0], 'K'),
        kdata = ([1.2770588127105103e-12, 1.4026821478062149e-12, 1.516282555183301e-12, 1.620583352077815e-12, 1.7166408037245634e-12, 1.890665705447366e-12, 2.04310837115349e-12, 2.183179666552586e-12, 2.309076385211653e-12, 2.5290745401773684e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=2) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 74,
    label = 'O2v6 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 146.5, 208.0, 288.0, 390.0, 518.5, 676.5, 1096.5, 1707.0, 2533.0, 3617.5, 5000.0], 'K'),
        kdata = ([9.670270910463037e-13, 1.111062523963313e-12, 1.2458685565460668e-12, 1.3731945507474576e-12, 1.493721757004841e-12, 1.6086595939893839e-12, 1.7175780664577484e-12, 1.9194356495947195e-12, 2.1094255672248263e-12, 2.283198533853397e-12, 2.443912949611661e-12, 2.5931985312219995e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=1) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 75,
    label = 'O2v6 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 121.0, 145.0, 204.5, 282.0, 380.5, 505.0, 659.0, 846.0, 1070.0, 1673.5, 2499.0, 3593.0, 5000.0], 'K'),
        kdata = ([6.7314229625738e-13, 7.463855562207963e-13, 8.18200670616892e-13, 9.603760695554293e-13, 1.099501540224222e-12, 1.2342348195013424e-12, 1.3657369755208555e-12, 1.4929298974356366e-12, 1.6153174109244158e-12, 1.7330017712723306e-12, 1.9638936634841136e-12, 2.178378925358563e-12, 2.3786881489716872e-12, 2.566044660686519e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=6) + O -> O2(w=0) + O, delta-v=6; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 76,
    label = 'O2v7 + O <=> O2v6 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 141.5, 205.0, 672.5, 1114.0, 1518.0, 1986.5, 2594.0, 3294.5, 5000.0], 'K'),
        kdata = ([1.1817054143517452e-12, 1.1485442932979629e-12, 1.1602585670502558e-12, 1.4633211814896677e-12, 1.7233791417089385e-12, 1.9318964610197408e-12, 2.1493345247071077e-12, 2.403695800025828e-12, 2.6693640655917642e-12, 3.235314333325247e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=6) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 77,
    label = 'O2v7 + O <=> O2v5 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 245.0, 478.0, 822.0, 1296.0, 2750.0, 5000.0], 'K'),
        kdata = ([1.2743331741576322e-12, 1.3880946450448095e-12, 1.4854091870970457e-12, 1.572027516709608e-12, 1.650164519378488e-12, 1.7904168849263416e-12, 1.9122207543422185e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=5) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 78,
    label = 'O2v7 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 273.0, 531.5, 898.5, 1389.0, 2836.0, 5000.0], 'K'),
        kdata = ([1.4509509425827806e-12, 1.5614091073731396e-12, 1.6574751007081035e-12, 1.7446369814941891e-12, 1.824393352349373e-12, 1.9696720385682924e-12, 2.098274523132522e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=4) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 79,
    label = 'O2v7 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 261.5, 511.0, 870.0, 1355.0, 2805.5, 5000.0], 'K'),
        kdata = ([1.4879826211916013e-12, 1.6078482240839995e-12, 1.7119281464898646e-12, 1.8056436036157264e-12, 1.8910006378345904e-12, 2.0457905989515343e-12, 2.1819744120618636e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=3) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 80,
    label = 'O2v7 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 153.0, 223.5, 315.0, 430.0, 746.5, 1196.5, 1825.0, 2649.0, 5000.0], 'K'),
        kdata = ([1.1579190919841136e-12, 1.2573234284670693e-12, 1.3486148999002327e-12, 1.4338999797111082e-12, 1.5136798476431413e-12, 1.6614891255236153e-12, 1.7951562479185909e-12, 1.921069880693528e-12, 2.037560522236119e-12, 2.2488053462612617e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=2) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 81,
    label = 'O2v7 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 148.0, 212.0, 295.0, 400.5, 533.0, 695.5, 1124.5, 1741.0, 2567.5, 3642.0, 5000.0], 'K'),
        kdata = ([8.231579880466038e-13, 9.437748313376746e-13, 1.05805925859854e-12, 1.1664628007703514e-12, 1.269811212103546e-12, 1.369223855963062e-12, 1.4643605940017351e-12, 1.6428620889136373e-12, 1.8133805996168468e-12, 1.971959125328931e-12, 2.1207421190208406e-12, 2.2608942229116918e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=1) + O, delta-v=6; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 82,
    label = 'O2v7 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 121.0, 145.5, 206.0, 284.5, 384.5, 511.0, 666.5, 855.5, 1081.5, 1688.0, 2514.0, 3604.0, 5000.0], 'K'),
        kdata = ([6.169686717791196e-13, 6.783675433204256e-13, 7.394563003870845e-13, 8.589379212739597e-13, 9.746196465603628e-13, 1.086458669793756e-12, 1.1954236520750254e-12, 1.3000947990926666e-12, 1.4009750105115872e-12, 1.4979230414087504e-12, 1.6879998327353425e-12, 1.8647858423555157e-12, 2.0302357572616873e-12, 2.1853774525015746e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=7) + O -> O2(w=0) + O, delta-v=7; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 83,
    label = 'O2v8 + O <=> O2v7 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 140.5, 202.0, 657.5, 1088.0, 1494.0, 1966.0, 2575.5, 3280.5, 5000.0], 'K'),
        kdata = ([1.0648807496734632e-12, 1.036220394210396e-12, 1.0481137562577752e-12, 1.3356191876895823e-12, 1.584795090607816e-12, 1.791817535900231e-12, 2.008865896425239e-12, 2.2626152352622446e-12, 2.5295244281101434e-12, 3.1024007062137204e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=7) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 84,
    label = 'O2v8 + O <=> O2v6 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 148.5, 224.0, 1100.5, 2180.0, 3424.5, 5000.0], 'K'),
        kdata = ([1.3139520964331193e-12, 1.2923608679262263e-12, 1.2927717255886329e-12, 1.4462307101543817e-12, 1.571977112073553e-12, 1.673865225566508e-12, 1.7711931829012957e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=6) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 85,
    label = 'O2v8 + O <=> O2v5 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 166.0, 279.5, 1216.0, 2144.0, 5000.0], 'K'),
        kdata = ([1.56467137873326e-12, 1.519325428356015e-12, 1.5120111616516233e-12, 1.6321227376840597e-12, 1.7212499804157673e-12, 1.8939621953331344e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=5) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 86,
    label = 'O2v8 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 165.0, 277.0, 2138.5, 5000.0], 'K'),
        kdata = ([1.6584083058758801e-12, 1.6185321476459173e-12, 1.6120099605602745e-12, 1.799498975714491e-12, 1.951632402947817e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=4) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 87,
    label = 'O2v8 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 297.0, 570.5, 949.5, 1447.5, 2887.0, 5000.0], 'K'),
        kdata = ([1.3209721137741552e-12, 1.4348368348290691e-12, 1.5341893136652854e-12, 1.6263302996416286e-12, 1.712157516958287e-12, 1.8717383547838005e-12, 2.0163018520517767e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=3) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 88,
    label = 'O2v8 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 154.5, 227.5, 321.5, 440.0, 763.0, 1219.0, 1850.5, 2673.0, 5000.0], 'K'),
        kdata = ([9.572162060741993e-13, 1.0491908879827948e-12, 1.1357759753258723e-12, 1.217402783623939e-12, 1.2952376878223182e-12, 1.4413118292744391e-12, 1.5761447078933553e-12, 1.7052331770064227e-12, 1.826545741008687e-12, 2.051008557071616e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=2) + O, delta-v=6; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 89,
    label = 'O2v8 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 149.0, 214.5, 300.0, 408.0, 543.5, 708.5, 1143.5, 1763.5, 2590.0, 3658.0, 5000.0], 'K'),
        kdata = ([7.309701204525878e-13, 8.358638740420899e-13, 9.358203079817352e-13, 1.0316399134867778e-12, 1.1229153656311534e-12, 1.2112292746025246e-12, 1.295794523254023e-12, 1.4561199537330231e-12, 1.6103885558054281e-12, 1.7552101787463754e-12, 1.8921585306120624e-12, 2.0220898582092153e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=1) + O, delta-v=7; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 90,
    label = 'O2v8 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 146.0, 207.5, 287.5, 389.0, 517.5, 675.0, 1094.0, 1703.5, 2530.0, 3615.5, 5000.0], 'K'),
        kdata = ([6.324219886933234e-13, 7.389876492048015e-13, 8.414339007868489e-13, 9.393202761022414e-13, 1.032494677424512e-12, 1.1225858744197506e-12, 1.2083349542288559e-12, 1.3689472660940737e-12, 1.521875393406089e-12, 1.6632634342437572e-12, 1.7949707917636569e-12, 1.9181030327803807e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=8) + O -> O2(w=0) + O, delta-v=8; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 91,
    label = 'O2v9 + O <=> O2v8 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 139.5, 198.5, 643.0, 1063.5, 1471.0, 1946.0, 2558.0, 3266.5, 5000.0], 'K'),
        kdata = ([9.698647228382309e-13, 9.451630010343095e-13, 9.569907492276665e-13, 1.2310241302104084e-12, 1.4707028862776486e-12, 1.6762878350071958e-12, 1.892968446150798e-12, 2.1465115749957393e-12, 2.414379052053198e-12, 2.9941105330688524e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=8) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 92,
    label = 'O2v9 + O <=> O2v7 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 136.0, 184.5, 345.5, 1392.5, 2299.0, 3513.5, 5000.0], 'K'),
        kdata = ([1.3327905127218616e-12, 1.2706261394308106e-12, 1.2341056194728213e-12, 1.2156702641081493e-12, 1.3617106916810582e-12, 1.4665970344973188e-12, 1.5771099468517854e-12, 1.685210674612263e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=7) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 93,
    label = 'O2v9 + O <=> O2v6 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 147.0, 215.5, 314.0, 462.0, 2609.5, 5000.0], 'K'),
        kdata = ([1.6431018659716605e-12, 1.5419340949819634e-12, 1.4828765303719289e-12, 1.4539530750488572e-12, 1.4474237723022624e-12, 1.621172391156082e-12, 1.757353986754016e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=6) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 94,
    label = 'O2v9 + O <=> O2v5 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 152.5, 230.0, 522.0, 2839.0, 5000.0], 'K'),
        kdata = ([1.7878076649920212e-12, 1.6774698391287956e-12, 1.6137231411779898e-12, 1.5710924707194416e-12, 1.7009684153432612e-12, 1.79246854047822e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=5) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 95,
    label = 'O2v9 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 152.0, 235.0, 1148.5, 2261.5, 5000.0], 'K'),
        kdata = ([1.4530685415922866e-12, 1.4292549529242004e-12, 1.4288131837937008e-12, 1.569629543616248e-12, 1.6829743358556868e-12, 1.8526757961675984e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=4) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 96,
    label = 'O2v9 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 272.5, 531.0, 898.0, 1388.5, 2835.5, 5000.0], 'K'),
        kdata = ([1.0716306526252192e-12, 1.2009546623431737e-12, 1.3178467963595548e-12, 1.4271082287703102e-12, 1.529721387890293e-12, 1.7229738273730712e-12, 1.900740704668789e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=3) + O, delta-v=6; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 97,
    label = 'O2v9 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 156.5, 231.5, 328.0, 448.5, 776.5, 1236.5, 1869.5, 2691.0, 5000.0], 'K'),
        kdata = ([8.325976343925382e-13, 9.185730603688497e-13, 9.997603855351084e-13, 1.0772144519629571e-12, 1.1512917604757715e-12, 1.2925454630596125e-12, 1.4246777764777673e-12, 1.5526360397370709e-12, 1.6743512387470912e-12, 1.9026190196723305e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=2) + O, delta-v=7; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 98,
    label = 'O2v9 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 151.0, 219.0, 307.5, 419.5, 729.0, 1172.0, 1797.0, 2622.0, 3680.0, 5000.0], 'K'),
        kdata = ([7.335418266257159e-13, 8.249058864590259e-13, 9.111222967382085e-13, 9.93368911359486e-13, 1.071897713068722e-12, 1.220180864984664e-12, 1.3573194311680433e-12, 1.4893348985116554e-12, 1.6134168491483285e-12, 1.7311048977637384e-12, 1.843062411660211e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=1) + O, delta-v=8; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 99,
    label = 'O2v9 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 147.5, 211.0, 293.5, 398.5, 692.0, 1119.5, 1735.0, 2561.5, 3638.0, 5000.0], 'K'),
        kdata = ([7.528704953636649e-13, 8.425386439231752e-13, 9.25821888259302e-13, 1.0033512617868977e-12, 1.0759994811164618e-12, 1.2094799709345747e-12, 1.3288367334865184e-12, 1.4404159121440808e-12, 1.5422353443918528e-12, 1.6362384287658815e-12, 1.7234885541851057e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=9) + O -> O2(w=0) + O, delta-v=9; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 100,
    label = 'O2v10 + O <=> O2v9 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 138.5, 195.5, 628.5, 1039.5, 1448.0, 1926.5, 2540.5, 3253.0, 4070.5, 5000.0], 'K'),
        kdata = ([8.915697578811742e-13, 8.703494231597768e-13, 8.822732971177196e-13, 1.143905655171484e-12, 1.375091860001243e-12, 1.5793082012901277e-12, 1.7960807302169096e-12, 2.0493820946654758e-12, 2.3184641202590993e-12, 2.6034691268199087e-12, 2.9047267267998287e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=9) + O, delta-v=1; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 101,
    label = 'O2v10 + O <=> O2v8 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 142.0, 200.5, 283.5, 405.0, 1574.5, 2445.0, 5000.0], 'K'),
        kdata = ([1.3356494479183666e-12, 1.2307291460295121e-12, 1.1711503042324054e-12, 1.1425735939423065e-12, 1.1383254886370893e-12, 1.2975837931862297e-12, 1.4030570643688942e-12, 1.6355509833641626e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=8) + O, delta-v=2; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 102,
    label = 'O2v10 + O <=> O2v7 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 124.0, 153.5, 233.5, 353.0, 536.0, 2909.0, 5000.0], 'K'),
        kdata = ([1.6908776591293531e-12, 1.5979657645952734e-12, 1.5272823647240658e-12, 1.4349304136743905e-12, 1.3881118406738273e-12, 1.373365417342182e-12, 1.5442770424681262e-12, 1.664634582017617e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=7) + O, delta-v=3; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 103,
    label = 'O2v10 + O <=> O2v6 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 127.0, 160.5, 254.0, 396.5, 618.5, 5000.0], 'K'),
        kdata = ([1.8783785212981744e-12, 1.7712036716896808e-12, 1.6906297008988776e-12, 1.584155641191092e-12, 1.5278173801108884e-12, 1.5046590923096857e-12, 1.6794732323020033e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=6) + O, delta-v=4; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 104,
    label = 'O2v10 + O <=> O2v5 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 141.5, 200.0, 403.5, 2442.5, 5000.0], 'K'),
        kdata = ([1.553842084457905e-12, 1.4878339263439792e-12, 1.4486165503797575e-12, 1.4267447048834267e-12, 1.5966968157678998e-12, 1.7340296927136651e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=5) + O, delta-v=5; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 105,
    label = 'O2v10 + O <=> O2v4 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 786.5, 1700.5, 3089.0, 5000.0], 'K'),
        kdata = ([1.1647873844519928e-12, 1.3523468551841842e-12, 1.5042297017753868e-12, 1.6512325036027888e-12, 1.7898757948781985e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=4) + O, delta-v=6; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 106,
    label = 'O2v10 + O <=> O2v3 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 175.0, 268.5, 523.5, 887.5, 1376.0, 2018.0, 2824.5, 5000.0], 'K'),
        kdata = ([9.196029430252839e-13, 9.883613798641841e-13, 1.053392998322794e-12, 1.1762313776617306e-12, 1.2926248037722513e-12, 1.4032386178834017e-12, 1.5109693842551648e-12, 1.6147662402273149e-12, 1.8125855878874773e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=3) + O, delta-v=7; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 107,
    label = 'O2v10 + O <=> O2v2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 161.5, 242.0, 344.5, 472.0, 813.0, 1284.5, 1922.0, 2739.0, 5000.0], 'K'),
        kdata = ([8.235616265803237e-13, 8.991287634579742e-13, 9.705317911883078e-13, 1.0389427133377605e-12, 1.1049899769586127e-12, 1.2310911057541472e-12, 1.350009829271433e-12, 1.4654518726624492e-12, 1.5758806072832034e-12, 1.7846164962844425e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=2) + O, delta-v=8; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 108,
    label = 'O2v10 + O <=> O2v1 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 157.0, 233.0, 452.5, 783.0, 1245.5, 1879.5, 2700.0, 5000.0], 'K'),
        kdata = ([8.597790474736971e-13, 9.315534173811015e-13, 9.98819388022985e-13, 1.122230714587965e-12, 1.234970232719239e-12, 1.3388346572204613e-12, 1.4379405018166012e-12, 1.5310711231236829e-12, 1.7032039773942655e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=1) + O, delta-v=9; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)

entry(
    index = 109,
    label = 'O2v10 + O <=> O2 + O',
    reversible = True,
    kinetics = KineticsData(
        Tdata = ([100.0, 229.5, 444.0, 769.5, 1227.5, 2681.5, 5000.0], 'K'),
        kdata = ([1.051437777476216e-12, 1.150670757932722e-12, 1.2332751721285025e-12, 1.3052053431311584e-12, 1.3687635036636097e-12, 1.4807190552634205e-12, 1.5754801023020145e-12], 'cm^3/(molecule*s)'),
        Tmin = (100.0, 'K'), Tmax = (5000.0, 'K')),
    shortDesc = 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4',
    longDesc = 'O2(v=10) + O -> O2(w=0) + O, delta-v=10; DegF=1/27 as stated for the paper fit. Source valid 50–10000 K; restricted to the thermo-valid range 100–5000 K for detailed balance; absences: 50–100 K and 5000–10000 K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.',
)
