import xarray as xr
import xesmf as xe
import numpy as np

modelID = ['CanESM5','CESM2-WACCM','GFDL-ESM4','INM-CM4-8','INM-CM5-0','MRI-ESM2-0','NorESM2-LM','NorESM2-MM']
sspID = ['ssp126','ssp245','ssp370','ssp585']
for i in range (0,len(modelID)):
    ds = xr.open_dataset('emidust_AERmon_'+modelID[i]+'_historical_r1i1p1f1_185001-201412.nc')
    ds_out = xr.Dataset({'lat': (['lat'], [-90.        , -89.0575943 , -88.11518097, -87.17277527,
               -86.23036957, -85.28795624, -84.34555054, -83.40314484,
               -82.46073151, -81.51832581, -80.57591248, -79.63350677,
               -78.69110107, -77.74868774, -76.80628204, -75.86387634,
               -74.92146301, -73.97905731, -73.03665161, -72.09423828,
               -71.15183258, -70.20942688, -69.26701355, -68.32460785,
               -67.38220215, -66.43978882, -65.49738312, -64.55497742,
               -63.61256409, -62.67015839, -61.72774887, -60.78533936,
               -59.84293365, -58.90052414, -57.95811462, -57.01570511,
               -56.07329941, -55.13088989, -54.18848038, -53.24607468,
               -52.30366516, -51.36125565, -50.41884995, -49.47644043,
               -48.53403091, -47.5916214 , -46.6492157 , -45.70680618,
               -44.76439667, -43.82199097, -42.87958145, -41.93717194,
               -40.99476624, -40.05235672, -39.1099472 , -38.16753769,
               -37.22513199, -36.28272247, -35.34031296, -34.39790726,
               -33.45549774, -32.51308823, -31.57068062, -30.62827301,
               -29.68586349, -28.74345589, -27.80104637, -26.85863876,
               -25.91623116, -24.97382164, -24.03141403, -23.08900452,
               -22.14659691, -21.2041893 , -20.26177979, -19.31937218,
               -18.37696266, -17.43455505, -16.49214745, -15.54973793,
               -14.60732937, -13.66492176, -12.7225132 , -11.78010464,
               -10.83769608,  -9.89528751,  -8.95287991,  -8.01047134,
                -7.06806278,  -6.12565422,  -5.18324614,  -4.24083757,
                -3.29842925,  -2.35602093,  -1.4136126 ,  -0.47120419,
                 0.47120419,   1.4136126 ,   2.35602093,   3.29842925,
                 4.24083757,   5.18324614,   6.12565422,   7.06806278,
                 8.01047134,   8.95287991,   9.89528751,  10.83769608,
                11.78010464,  12.7225132 ,  13.66492176,  14.60732937,
                15.54973793,  16.49214745,  17.43455505,  18.37696266,
                19.31937218,  20.26177979,  21.2041893 ,  22.14659691,
                23.08900452,  24.03141403,  24.97382164,  25.91623116,
                26.85863876,  27.80104637,  28.74345589,  29.68586349,
                30.62827301,  31.57068062,  32.51308823,  33.45549774,
                34.39790726,  35.34031296,  36.28272247,  37.22513199,
                38.16753769,  39.1099472 ,  40.05235672,  40.99476624,
                41.93717194,  42.87958145,  43.82199097,  44.76439667,
                45.70680618,  46.6492157 ,  47.5916214 ,  48.53403091,
                49.47644043,  50.41884995,  51.36125565,  52.30366516,
                53.24607468,  54.18848038,  55.13088989,  56.07329941,
                57.01570511,  57.95811462,  58.90052414,  59.84293365,
                60.78533936,  61.72774887,  62.67015839,  63.61256409,
                64.55497742,  65.49738312,  66.43978882,  67.38220215,
                68.32460785,  69.26701355,  70.20942688,  71.15183258,
                72.09423828,  73.03665161,  73.97905731,  74.92146301,
                75.86387634,  76.80628204,  77.74868774,  78.69110107,
                79.63350677,  80.57591248,  81.51832581,  82.46073151,
                83.40314484,  84.34555054,  85.28795624,  86.23036957,
                87.17277527,  88.11518097,  89.0575943 ,  90.        ]),'lon': (['lon'],  [0.  ,   1.25,   2.5 ,   3.75,   5.  ,   6.25,   7.5 ,
                 8.75,  10.  ,  11.25,  12.5 ,  13.75,  15.  ,  16.25,
                17.5 ,  18.75,  20.  ,  21.25,  22.5 ,  23.75,  25.  ,
                26.25,  27.5 ,  28.75,  30.  ,  31.25,  32.5 ,  33.75,
                35.  ,  36.25,  37.5 ,  38.75,  40.  ,  41.25,  42.5 ,
                43.75,  45.  ,  46.25,  47.5 ,  48.75,  50.  ,  51.25,
                52.5 ,  53.75,  55.  ,  56.25,  57.5 ,  58.75,  60.  ,
                61.25,  62.5 ,  63.75,  65.  ,  66.25,  67.5 ,  68.75,
                70.  ,  71.25,  72.5 ,  73.75,  75.  ,  76.25,  77.5 ,
                78.75,  80.  ,  81.25,  82.5 ,  83.75,  85.  ,  86.25,
                87.5 ,  88.75,  90.  ,  91.25,  92.5 ,  93.75,  95.  ,
                96.25,  97.5 ,  98.75, 100.  , 101.25, 102.5 , 103.75,
               105.  , 106.25, 107.5 , 108.75, 110.  , 111.25, 112.5 ,
               113.75, 115.  , 116.25, 117.5 , 118.75, 120.  , 121.25,
               122.5 , 123.75, 125.  , 126.25, 127.5 , 128.75, 130.  ,
               131.25, 132.5 , 133.75, 135.  , 136.25, 137.5 , 138.75,
               140.  , 141.25, 142.5 , 143.75, 145.  , 146.25, 147.5 ,
               148.75, 150.  , 151.25, 152.5 , 153.75, 155.  , 156.25,
               157.5 , 158.75, 160.  , 161.25, 162.5 , 163.75, 165.  ,
               166.25, 167.5 , 168.75, 170.  , 171.25, 172.5 , 173.75,
               175.  , 176.25, 177.5 , 178.75, 180.  , 181.25, 182.5 ,
               183.75, 185.  , 186.25, 187.5 , 188.75, 190.  , 191.25,
               192.5 , 193.75, 195.  , 196.25, 197.5 , 198.75, 200.  ,
               201.25, 202.5 , 203.75, 205.  , 206.25, 207.5 , 208.75,
               210.  , 211.25, 212.5 , 213.75, 215.  , 216.25, 217.5 ,
               218.75, 220.  , 221.25, 222.5 , 223.75, 225.  , 226.25,
               227.5 , 228.75, 230.  , 231.25, 232.5 , 233.75, 235.  ,
               236.25, 237.5 , 238.75, 240.  , 241.25, 242.5 , 243.75,
               245.  , 246.25, 247.5 , 248.75, 250.  , 251.25, 252.5 ,
               253.75, 255.  , 256.25, 257.5 , 258.75, 260.  , 261.25,
               262.5 , 263.75, 265.  , 266.25, 267.5 , 268.75, 270.  ,
               271.25, 272.5 , 273.75, 275.  , 276.25, 277.5 , 278.75,
               280.  , 281.25, 282.5 , 283.75, 285.  , 286.25, 287.5 ,
               288.75, 290.  , 291.25, 292.5 , 293.75, 295.  , 296.25,
               297.5 , 298.75, 300.  , 301.25, 302.5 , 303.75, 305.  ,
               306.25, 307.5 , 308.75, 310.  , 311.25, 312.5 , 313.75,
               315.  , 316.25, 317.5 , 318.75, 320.  , 321.25, 322.5 ,
               323.75, 325.  , 326.25, 327.5 , 328.75, 330.  , 331.25,
               332.5 , 333.75, 335.  , 336.25, 337.5 , 338.75, 340.  ,
               341.25, 342.5 , 343.75, 345.  , 346.25, 347.5 , 348.75,
               350.  , 351.25, 352.5 , 353.75, 355.  , 356.25, 357.5 ,
               358.75])})
    regridder = xe.Regridder(ds, ds_out, 'bilinear')
    dr = ds['emidust']
    dr_out = regridder(dr)
    dr_out.to_netcdf('regrid_emidust_AERmon_'+modelID[i]+'_historical_r1i1p1f1_185001-201412.nc')
