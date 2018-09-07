import numpy as np
#from CPG_core.quadruped_osc.oscillator_2_sin import oscillator_nw        #quaquepade
from CPG_core.snake_osc.snake_oscillator_2 import oscillator_nw  #snake
#from CPG_core.quadruped_osc.oscillator_2 import oscillator_nw
#from CPG_core.butterfly_osc.butterfly_oscillator_5_sin import oscillator_nw

#from CPG_core.bigdog2_osc.bigdog2_oscillator_2 import oscillator_nw


position_vector= [0.23656012185586192, -0.9970809182081581, 0.774396674822355, 0.31000955892983706,
                  -0.49557014420500645, -0.9584473826208844, 0.6202572199721552, 0.09363779917529014, -0.4732123061017435, 0.8375333464294166, 0.9211128381386937, 0.2945791797540447, 0.8753681375428313, 0.9385986406504117, 0.1450880183917258, -1.1923746916542486, -1.2697994651998785, 0.20651942841342397, 0.6740348026658651, 0.20150838295981566, -0.06674515582547791, -0.13388646352309652, 1.5205325690752272, 0.17152076670537308, 0.05525899668030899, -0.14344020741644314, -0.9909686093795667, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1]

position_vector =[0.2127980599202492, -0.944064089630757, 0.5272514586758441, 0.7746905487256992, 0.9194133827424442, -0.5329483396675674, 0.1466389504478953, 0.40877316520001017, 0.09106409990121986, -0.916529744504491, -0.7173599518199573, -0.5482984750237796, 0.8798611086858199, 0.2459424423149077, -0.18855453851686677, 1.2272948534512405, 0.211294726450167, 1.2108682550970018, 0.29975916369814115, -1.093245387089748, 0.1830964897944887, -1.0297981579062045, 0.3801860432766482, -0.7267814442814976, 0.9149231302163434, 0.0811744167206947, 1.1104026139146177]


position_vector =[0.5374599941974265, 1.656074345303363, -1.7920405686614518, 0.36516167563233903, -0.28410367957244825, 1.3899568769228767, -1.68022354933243, -0.7635215883298008, -0.8077468560778978, -1.4212586842955526, -1.4139011730631772, -0.037375077965509096, -1.4200410155179215, -1.3668612925063695, 1.2005257659131385, 0.12795409290654636, 0.7736134759621711, -0.1276188968821821, 0.23430410108765876, -0.0989197393204555,
                  -0.11675519729139894, 0.04729760924906379, -1.453425237705716, -0.7297822976983444, 0.9149231302163434, 0.0811744167206947, -0.3127508652263906]


position_vector =[0.4209433905019311, -1.3968109452684754, 1.8098156051568441, 1.6847954525077853,
                  -1.311929557004543, 1.473478572730441, -1.6630349628347934, 1.8721640754351903,
                  -0.895386802419043, -0.6262136874874034, -1.4139011730631772, -0.037375077965509096,
                  -1.4200410155179215, -0.6790253776938182, -0.927974989450087, -0.9188338159431343, -0.09424439460808842, 0.07817714519813836, 1.3618525322368162, 0.5213897736719444,
                  -1.5496246372612419, 0.6313006841358848, -0.9436394289423488, -0.8464548232578526, -0.5767207977183963, 0.916455638124809, 1.0760629021983275]
# position_vector = np.zeros(27)
# position_vector[0]=1
# for i in range(1,14):
#     position_vector[i] = 1

#snake  侧着走
position_vector =[0.44352591933186664, 0.5856138166539036, -1.0873626676932258, 0.548247337872537, -0.95419125310347, 1.6752249854546903, -1.1163359090272045, 1.8764078368624597, -0.8946916197516748, 1.9909929576955165, -0.42944960328557713, 0.10832168779380558, -1.1457664410447541, 1.1004710431306495,
                  -0.4164716893342981, 0.6951986377497454, 0.10333143011476476, 1.5441552609822868, 1.0456936830675168]

#snake
position_vector = [0.44352591933186664, -0.13051537542314628, -1.0873626676932258, 0.548247337872537, -0.95419125310347, 1.6752249854546903, -1.1163359090272045, 1.8764078368624597, -0.8946916197516748, 1.9909929576955165, -0.42944960328557713, 0.10832168779380558, -1.1457664410447541,
                   1.3833667827197185, -0.18838150126811515, 0.6951986377497454, -1.0123759649649628, 0.6145444965947173, 1.0456936830675168]

#qurapade 17:32
# position_vector =[0.3830892032450691, 1.8626539585127104, 0.12668937339856434, -1.186792851868456, -0.8328265914690651, 0.2433819330429663, -0.6251034751321263, 0.3550220938911339, 1.8889234941767619, -0.23345857612433685, 1.6934940731311383, 1.7110878101504539, 1.589482477871924, -1.3170663301937693, -0.35240135281722806, 0.691712230139574, 0.2287463501350725, 0.5340628292785232, 1.4349375474368373, 1.411415096070534, -0.3320301115077877,
#                   -0.23380243332411937, 0.29791391732888783, -0.5256292426176661, -0.31724755502398927, 0.6868486084717764, -1.2468753044387562]
#


position_vector = [0.9252993847079439, -0.23529666595463916, 0.47046205695846877, -0.9096929710639923, -0.5719695231298698, 0.9768096756376117, -0.735810186468002, 0.9354153121348276, -0.3033102398185308, 0.028884882810709334, 0.46777503021612743, 0.7028336544870608, -0.8199334052622633, 0.8359378405649813, 0.747189917416331, 0.6497397821834028, -1.3217508842892172, -0.1799477408459862, 0.18962471022622718, -1.5461534442502345, 1.059765108343878, -0.3320301115077877, 1.4659615710501277, -0.6066826416560194, 0.6498454170090691, -0.4667936015079144, -1.3026945477137106, -0.700102566390663, -2.0622009323029826, 2.838821980957891, 0.7454602918870608, -0.26561268712750064, 0.9423235787873239,
                   -0.33926840535755165, 2.6663414231416027, 0.648973015788278, 0.45271253236343556, 0.5360949767878362, 2.50351854783512, -2.4804582027064943]
position_vector = [0.43355534342894686, -0.6291062151173377, 0.7793761980393781, -0.7056751198155546, -0.986859438188314, 0.8673859148521691, 0.12603741438557736, -0.9334631968729856, -0.6433372692437356, 0.20261321917552855,
                   0.14240288381526245, 0.6373312106475701, -0.9191002453748132, -0.8534730577722334, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1]

position_vector = [0.9173704470842545, 1.8757480589886844, 1.8027811693799154, -1.9027331044115612, 1.6011269726457071, 0.7742241244243635, 0.6129145509808294, 1.098035407067393, 1.6652877009928435, -1.7682323463220193, -1.3261370736821914, 0.5126077720139159, 0.20694537629273757, 1.0491197959905758, 0.8324003668419717, 1.4496576346943852, -0.801890156565281, -1.4549692171631332, 1.320277223958132, 0.8287043767350322, -0.2920787969949852, 0.007059335275624967, -0.26211955604930015, 0.4105417150805559, -1.4522789339044255, -2.203981332269547, -2.0107589589756465, 1.0531484775614386, -1, -1, -1, 1, 1, 1, -1, -1, -1]


# GA_2
position_vector = [0.4787101675465735, 1.4886269683264208, 0.01635411858973157, -1.6206785462817241, 0.8716434386197909, -1.1102794039121213, 1.6216157544534848, -0.19050691108795004, 1.7753622329821126, 1.0485611742743632, 1.8065560676398258, 1.7352036205575903, 1.7374270441590105, 0.5969403661628614, -1.0918844589876986, 0.14006780025431254, -0.16485211757632623, -0.07248275340476695, 1.1854858740331828, 0.8888382335906404, -0.34660298843603854, 0.31755839939857067,
                   0.007388868100693058, -0.3285394449607004, -0.6304421480787882, 1.564823395625297, 0.5849326371057528]

position_vector = [0.7093947807097245, -1.3419359861672198, 0.6217178372755718, 1.0215712660204652, -0.8407724336791662, 1.8940015851917962, -0.8793071829364183, 1.97885102955741, -1.491527317228412, 1.6213707514608817, -0.31479375723463665, 1.2386359107029046, 1.7223054622799476, -0.5722756377237563, 0.835141967224144, -0.4687610277332508, -0.7842743056943026, -0.6334551954175893, -0.8745375051496882, 0.8651714886592257, 0.12215499674679986, 0.27939286895995563, -0.18955068938070285, -0.12173879881896066, 1.0250748523062638, 0.39396131815462176, -0.591402550840603, 0.01717340569348469, 2.570419669951252, 0.18298945332942518, 1.0034502078885605, 0.1322115853256416, -3.082670707615917, -1.8465271417324483, -2.4171833780872527, 2.4341276042333937, 0.5643430082273131, 1.585776381273682, -0.37279065957660595, 1.5134735333200862]

position_vector = [0.9173704470842545, 1.8757480589886844, 1.8027811693799154, -1.9027331044115612, 1.6011269726457071, 0.7742241244243635, 0.6129145509808294, 1.098035407067393, 1.6652877009928435, -1.7682323463220193, -1.3261370736821914, 0.5126077720139159, 0.20694537629273757, 1.0491197959905758, 0.8324003668419717, 1.4496576346943852, -0.801890156565281, -1.4549692171631332, 1.320277223958132, 0.8287043767350322, -0.2920787969949852, 0.007059335275624967, -0.26211955604930015, 0.4105417150805559,
                   -1.4522789339044255, -2.203981332269547, -2.0107589589756465, 1.0531484775614386, -1, -1, -1, 1, 1, 1, -1, -1, -1]
#position_vector = [0.38182888266979986, 1.898587589077191, 1.3430883796872108, 1.9537559494204708, 0.19471857288334915, -1.589659813688641, 1.556965666043654, -0.19536326195264486, 0.9297531773888741, 1.4192113911692648, 0.7327260207886588, -0.8252762394916086, 0.4727863421862999, -0.16904427957841642, -0.70211753905422, 2.3646047559837555, 2.4507241189070834, -1.5672908387839197, 1.352804284416079, 0.525727871691961, -2.715386517370129, -0.07192896309616659, -1, -1, 1, 1, 1, 1, 1]
position_vector = [0.8700919445712163, 1.0963204915585703, 1.5037062829799592, 0.7345921522874703, 1.8712363529422533, -0.19319412165009542, 0.4848631944987458, -0.48672418263314876, -0.907968865561879, 0.13028230107532845, 0.8636568125592099, -0.3440200764656782, 0.6446489500102368, -0.0973841588751474, 1.2463108312830022, 0.4100980677362691, 1.3914794230154222, -0.11847395380616499, -0.29263067122178543, 2.298211169677619, -2.887970764878024, -0.0026772123033285133,
                   -0.44059174491834696, -2.0920764848946707, -2.8817415199593626, 1.0240092959194138, -0.6485672451027922, 0.6192674342655362]

position_vector =[0.9823318542968837, -0.13860420458969847, 1.7442077466292831, 1.5460960878311885, 1.5614080767226546, -0.19319412165009542, 0.6712474083024977, 0.7763256345303641, -0.907968865561879, 0.13028230107532845, 0.8636568125592099, -0.3440200764656782, 0.6446489500102368, 1.4732600619200666, 0.5587536426244841, 0.4100980677362691, 1.3914794230154222, 1.2405431899550874, 0.45856295259362323, 2.298211169677619, -2.887970764878024, 0.28928351057055, 0.28646178721884796,
                  -2.85788475491691, -0.6741664068852793, -0.7925888621161143, -1.5042096532017069, -1.380009563738384]

position_vector =[0.8499695820011207, 0.20240118699205878, -0.6382310291886104, -1.7608446543984226, -1.7452052874246538, -1.1588823701548168, -0.8869909374325262, -1.7984081884426848, -0.681140625412409, -0.9117991592229684, 0.6071887349025986, 0.3499050858939181, 0.5581357348695186, 0.32772813648876054, 0.5503644252665123, 1.2775038102597551, -0.2147313999368894, 0.2608647484610125, -0.061458521939208755, 0.8287043767350322, -1.874027129868295, 0.007059335275624967, -0.26211955604930015, -2.628621387642264, -0.31958105291559846, 3.107532911081462, -0.5264837439467951, 0.08351178154647343, 1, -1, -1, -1, 1, -1, 1, 1, 1]


# CellrobotEnv  5sin
position_vector = [0.7076894656605008, 0.17096603687654977, -0.599482783638067, -1.6550654116436474, -1.2548891496980792, 1.4690090047286004, -1.1004751409111666, 1.286460004495415, 1.6895902934542324, 1.2090530486124336, 0.7465456836087818, -1.4012239754719218, -1.6256362547197982, -1.3219706557152646, -0.5653057331615228, -0.09695755229404712, -0.6042399728397487, -0.3729542310795899, -0.4755778262979149, -1.5522652110423025, -0.1884949298824421, -1.1026007974718601, -0.35787338190967577, -0.9666695591016446, 1.0713877624917623, -0.27037321560156746, -0.3328766407300727, 0.537816038381413, 1.0278336050008212, 2.7625832543246025, -0.34463933192700846, 1.3952764780717501, 2.302477529021867, 2.8312311733620925, 0.2954224156712506, 0.00298649545113161, 0.38054916010492246, -3.0784544227748682, 1.3356839498360644, 1.524467314526082, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1]
# CellrobotEnv 2sin
position_vector = [0.792637075294669, -1.3419359861672198, 0.6217178372755718, 1.0135928006506747, -1.9464908023077476, 1.8940015851917962, -0.8793071829364183, 1.97885102955741, -1.3420059811058382, 0.13511236237011515, -0.31479375723463665, 1.2386359107029046, 1.7223054622799476, 0.4217719000431672, 0.835141967224144, -0.2978427027352426, -1.0181893780204452, 1.2281043498562396, 0.13168316549697145, 0.8741358965049222, 0.08710574107385805, 0.20043027791376833, -1.4524275626628733, 0.031423632920919875, 0.17564136544406228, -0.3481789164298186, -0.1134329881325149, -0.3390381014758419, -2.9821469243361896, -0.6958905195182932, 1.4922597347160407, 0.1322115853256416, -3.082670707615917, -1.8465271417324483, -1.8357317538831763, -0.4715433591620708, -0.9946364304020561, -1.0916128900283777, -0.37279065957660595, -2.381538574815667]

# Snake 2_sin
position_vector = [0.8700919445712163, 1.0963204915585703, 1.5037062829799592, 0.7345921522874703, 1.8712363529422533, -0.19319412165009542, 0.4848631944987458, -0.48672418263314876, -0.907968865561879, 0.13028230107532845, 0.8636568125592099, -0.3440200764656782, 0.6446489500102368, -0.0973841588751474, 1.2463108312830022, 0.4100980677362691, 1.3914794230154222, -0.11847395380616499, -0.29263067122178543, 2.298211169677619, -2.887970764878024, -0.0026772123033285133, -0.44059174491834696, -2.0920764848946707, -2.8817415199593626, 1.0240092959194138, -0.6485672451027922, 0.6192674342655362]

# Snake 5_sin
position_vector = [0.9173704470842545, 1.8757480589886844, 1.8027811693799154, -1.9027331044115612, 1.6011269726457071, 0.7742241244243635, 0.6129145509808294, 1.098035407067393, 1.6652877009928435, -1.7682323463220193, -1.3261370736821914, 0.5126077720139159, 0.20694537629273757, 1.0491197959905758, 0.8324003668419717, 1.4496576346943852, -0.801890156565281, -1.4549692171631332, 1.320277223958132, 0.8287043767350322, -0.2920787969949852, 0.007059335275624967, -0.26211955604930015, 0.4105417150805559, -1.4522789339044255, -2.203981332269547, -2.0107589589756465, 1.0531484775614386, -1, -1, -1, 1, 1, 1, -1, -1, -1]


# Snake 2_sin PSO

# cellrobot 2sin
position_vector =[0.9989469253246996, -1.0285380533868027, 0.6217178372755718, 1.0135928006506747, -0.8407724336791662, 1.8940015851917962, -0.8793071829364183, 1.97885102955741, -0.46453329038782315, 1.7346406601513076, 1.1261881055600211, 0.5220499790138744, 1.9366001181828367, 0.4217719000431672, 0.7449850583298718, -0.14559423694556517, -0.6890988694158419, -0.21922678649225058, 0.13168316549697145, 0.8741358965049222, 0.08710574107385805, 0.7778925025027159, 1.3321706369077728, -0.6640916161282513, 1.38313238198158, 0.4874564466257052, -1.3026945477137106, -0.3390381014758419, -2.9821469243361896, -0.6958905195182932, 1.4922597347160407, 0.1322115853256416, -3.082670707615917, -2.832152880406684, 1.7438737750798579, -0.4715433591620708, -0.9946364304020561, -1.0916128900283777, -0.37279065957660595, -2.317993113973975]

position_vector = [0.7224228963341959, -1.3419359861672198, 0.6217178372755718, 1.0135928006506747, -0.8407724336791662, 1.8940015851917962, -0.8793071829364183, 1.97885102955741, -0.46453329038782315, 1.6213707514608817, 1.1261881055600211, 0.5220499790138744, 1.9366001181828367, 0.4217719000431672, 0.7449850583298718, -0.14559423694556517, -0.24883481923443784, -0.33610773349852474, 0.13168316549697145, 0.8741358965049222, 0.08710574107385805, 0.20043027791376833, -0.30372075095150364, -1.1842969747484549, 0.17564136544406228, 0.48495004601732034, -1.3026945477137106, -0.3390381014758419, -2.9821469243361896, -0.6958905195182932, 1.4922597347160407, 0.1322115853256416, -3.082670707615917, -2.832152880406684, 1.7438737750798579, -2.9893231181715363, -0.9946364304020561, -1.0916128900283777, -0.37279065957660595, 1.5134735333200862]

position_vector = [0.792637075294669, -1.3419359861672198, 0.6217178372755718, 1.0135928006506747, -1.9464908023077476, 1.8940015851917962, -0.8793071829364183, 1.97885102955741, -1.3420059811058382, 0.13511236237011515, -0.31479375723463665, 1.2386359107029046, 1.7223054622799476, 0.4217719000431672, 0.835141967224144, -0.2978427027352426, -1.0181893780204452, 1.2281043498562396, 0.13168316549697145, 0.8741358965049222, 0.08710574107385805, 0.20043027791376833, -1.4524275626628733, 0.031423632920919875, 0.17564136544406228, -0.3481789164298186, -0.1134329881325149, -0.3390381014758419, -2.9821469243361896, -0.6958905195182932, 1.4922597347160407, 0.1322115853256416, -3.082670707615917, -1.8465271417324483, -1.8357317538831763, -0.4715433591620708, -0.9946364304020561, -1.0916128900283777, -0.37279065957660595, -2.381538574815667]

position_vector = [0.26126929443844465, 1.8086745907234585, -1.8040792802454164, -0.08005612631830594, 0.24572736717588156, -0.6871847472804385, -1.8796633522863797, 1.5717253244651253, -0.9794658650367163, -1.6586929748491124, 1.309919091723943, 1.1667353667452138, -0.36197487215174595, -0.44215431954863904, 0.3198661118931052, 0.4008962704297203, -0.02668112718620108, -1.004708259362947, -0.16689872159112973, 0.29705179274472715, -0.3135765207260064, -0.47616049597284404, 0.42783666877824555, -0.13169005349736085, 0.9909674010044602, -1.0212467691086409, -0.7722938778906653, 0.036862268354303174, -1.3124111635496023]

position_vector = np.zeros(29)
position_vector[0]=1
for i in range(1,15):
    position_vector[i] = 1
    
## 修改模型后
## snake 2
position_vector = [0.24439871034803845, -1.5312753106875245, 1.1242956744350385, 1.2209807751225936, 1.3358582028175265, 1.0018950281383106, 0.783268746577066, 0.769605007776056, -1.6035667518385184, 1.4215317702016113, -0.6082573530718346, 0.6968553629139653, 0.24506523609463193, -1.2000093481820913, 0.42935879749640765, -1.35431211236549, -0.7651899494755541, -0.29776970616265186, -1.4978580212486545]


##cellrobot 2
#position_vector = [0.6311064806315902, 0.6068302518044875, 1.31309978249537, -0.7402723082008711, 1.2161905425095387, 0.09114795866162595, 1.1069388729164498, 1.4630866716927984, 0.7004536668539894, 0.32872222072026736, 1.056440660973784, -0.3929857149017053, -0.9763448088106252, 0.6163989622835402, 0.07813771886977695, -0.03727988756164624, 0.1378805601648847, 0.9282063238510654, 1.2905927941601156, 0.45621780808233847, 0.795050893829989, 0.4498919930195351, 1.0445490329020943, -1.1344600090110242, -0.15525905059315925, -0.06584023774042946, -0.23465523405988686]

# ## cellrobot 2_sin
position_vector =  [0.7160772004134695, 1.449788602713649, -0.9444709768865467, 1.9226039303996685, -0.7195786266883788, -0.48693894199941257, -1.0023404777911131, -1.255803801428776, -0.10832021748311993, 0.12032736902575447, 1.3107410659259107, -1.733034818799517, -1.8273586631100498, -0.8243084960820699, -0.2753712492588603, 1.3935314705414097, -0.013745970722634544, -0.17299120549005131, 0.676711079194318, -1.1631269687422492, 0.7862446910000074, -0.9983468112836941, 0.5100487236742355, 0.5956808239225548, -1.4216037969614124, -0.1891311125211499, -0.8572815810543926, -1.7756580904111787, 0.13803902543318047, 2.156888493754228, -0.36210986505301834, 2.0229175755562965, -2.9629475245620434, 2.8993152693887705, -1.6480240558763901, -1.157254438383839, -0.8857725102550429, -2.5794128272715766, 2.9970844770572302, 2.849769678295009]
#
#
# #cellrobot 5_sin
# position_vector = [0.8761049622288921, 0.8235982678176086, 1.2207123953271708, -0.2685522190894587, 0.5885190595513565, -1.4991858027592588, -0.5801631743340452, 0.3974532520837428, -1.4260776380664684, 1.0341905564013238, -0.23436110760073436, 0.5833116181293643, 0.9633687592656957, 0.24434506801376754, -0.5510969564640666, 0.3570277615531865, 0.9993100436744635, -0.6545153654321757, -0.014608218617075286, 0.7114680858830162, -0.0015192759138684675, -0.3491436453743417, 0.45004066446377555, 1.2762833769919402, -0.8910429274639816, 0.2376427834054775, 1.2232765418646134, 1.5743911757581586, -0.03673852745141293, 1.7146661679586161, -0.06931182230425481, -2.2162567792007097, -3.0992492745224838, 1.2626013682717696, -1.8872788578846975, -1.638875227254776, -1.2966577541058886, -0.8227424695974972, 2.7534765431577144, 2.008017864427716, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1]
#
# #cellrobot2 2
# position_vector =[0.747282613503732, -1.7099716220729797, -1.0181926205606961, 1.0859538649967444, -1.175535688640272, -1.1686631312850486, -1.9056702441266737, -0.4547940613742867, -1.0479871948759207, -0.23732590484041927, 0.9584512160363196, 1.883473465619904, 1.2109996039529318, -1.3062371608380703, 0.37073043137469375, 1.0526135277022135, 0.5195383016424149, -0.8395328644841518, 0.07684444843395766, -0.31768577882339, -0.8611227474096566, -0.2263291307889168, 1.139565423588769, -0.6945735556890752, -0.31724755502398927, 0.5916049502568645, -0.6124680479911359]
#
# # cellrobot2 2_sin
# position_vector =  [0.9131726267862932, 1.7146640917449805, 0.25272744788525436, 1.2928644752403295, -0.7195786266883788, -0.29717021781056063, -0.9638266218755569, 0.007558551684622383, 1.1813747569527862, 1.6987559074871559, 0.8862291800806545, 0.6514031359767372, 0.6632373005490648, 1.209456773375691, -0.2747180176608839, 1.3935314705414097, -0.016094102006418476, -0.17299120549005131, 0.6794647453017815, -1.1551495026065997, 0.7860267338088724, -0.9983468112836941, 0.5100487236742355, 0.5956808239225548, -1.4216037969614124, -0.1891311125211499, -1.4309282641732934, -0.3667348100510015, 2.583057128419042, -2.7292553050077086, -0.5583174899952588, 2.984977284287041, 0.4635504819864278, -3.0553704338306464, -1.1866971248467573, -3.122800461835441, 0.844868816943336, -3.112608473841977, 0.7578429778033056, -2.92097908552405]
# # cellrobot2 5_sin
# position_vector =[0.9903626338142754, -1.852339270681214, 0.6974865929568237, -1.3740249785531233, 0.611593511309438, -1.4991858027592588, -0.5801631743340452, 1.7893295372493871, -1.8263695940242344, -0.6271853794681936, -1.0899214449392165, -1.449793800670561, 1.4140720322702884, 0.48722535958734925, 0.0905331797994402, -0.09944100814797041, -1.094767260516062, -0.4022332881357469, -1.557034347182505, -0.3633674705122547, -0.14007661350539802, 0.8260176644479071, -1.3109689196153689, -1.5246563547339667, -0.5777994463695378, 0.8127081565780436, 0.8136325758760803, -1.3297526368377355, -2.2194823053797714, -1.9707195257237116, 2.3726141252987842, 1.4343662414976137, 1.1716712123258723, 0.16969415056787174, 0.981024504446351, 0.8653409311393876, -1.5090819694062723, -0.5021633977378963, -0.699272597751158, -0.47649746950788296, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1]

position_vector = [0.25118209547160864, 1.5590066060199308, -1.713145002305282, -0.8641661339812692, -1.9957916389539747, 0.67157712338541, 1.7053192866442526, -0.21014015251250304, 1.3843293136001793, -0.3469650311314836, -0.5958522053194901, 1.4033882098277903, -1.3622458445567474, 1.1934414696060753, -0.5215473542725582, 0.208747139066922, -0.11980542411379047, -0.9511214813988587, 0.4225175562023997, 1.252324669858377, 0.16012344905696407, -0.9779240079822195, -0.3355885368867828, -0.18956870893216538, -0.6202273145022256, 0.868392303094355, -1.2468753044387562]
position_vector = [0.37102413545413016, 1.3910881749130488, 0.12668937339856434, -1.9330408003422854, -1.5691336422080568, 0.6822527451421536, 0.8485303685004038, 1.7636326994574274, 1.3843293136001793, -0.3469650311314836, -1.325167830811286, 1.4033882098277903, -1.3622458445567474, 1.1934414696060753, -0.5215473542725582, 0.208747139066922, -0.5401414984839323, -0.5460350659448774, 0.028048780772617965, 0.168372134468058, 1.3282240894901656, -0.9779240079822195, -0.33141067931205603, 0.29852261565871974, -0.6202273145022256, 0.868392303094355, -1.2468753044387562]
position_vector = [0.31544638304456235, 1.7942256384543018, -1.713145002305282, -0.8641661339812692, -1.9957916389539747, 0.67157712338541, 0.8485303685004038, -0.9416088517071476, 0.5838604849927167, -1.8148276231230374, -0.5958522053194901, -0.293118184869576, -1.3622458445567474, 1.0424919134539943, -0.5215473542725582, 0.12795409290654636, 0.6107886947706076, -0.5651548484732758, 0.009373835744095782, 1.4275461091182817, 0.5470285002015678, -0.21635812687113387, -0.6719004553387402, 0.8570867180292807, 0.012227863420083418, 0.5971213653767644, -0.8765527787413433]

position_vector =  [0.30238227791178307, 1.1461614367101216, -1.1009668751096093, -1.5169115611180701, -1.8219020876930485, 1.2807389283934758, -0.9905200642152812, -1.345306937709823, -0.9887565319242282, 1.865171249536699, -1.4414133701294753, 1.001722588596044, -1.444105228794247, 1.1120946935342784, -0.1491069940484817, 0.039526591164930736, -0.005272988742146323, -0.16279351777490336, -0.7039709413289968]


env_name = 'CellrobotSnakeEnv-v0' #'CellrobotButterflyEnv-v0' #'Cellrobot2Env-v0'# 'CellrobotSnakeEnv-v0' CellrobotBigdog2Env-v0
result=oscillator_nw(position_vector, max_time=10.0, fitness_option=4, plot = False, log_dis = False, render=False, env_name=env_name )

print('fitness = ', result['fitness'])
print('x distance = ', result['x_distance'])