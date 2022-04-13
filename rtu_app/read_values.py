from rtu_app.utility import get_value_syn, get_ip


def update_read_vars(rtu_read_vars):
   ip=get_ip()
   lip=ip[-3:].lstrip('.')
   for i in range(len(rtu_read_vars)):
      rtu_read_vars[i]['addr']=lip
      rsp=get_value_syn(rtu_read_vars[i]['index'])
      if rsp is not None:
            rtu_read_vars[i]['value']=float("{:.2f}".format(rsp))

def init_read_vars(rtu_read_vars):
      ip=get_ip()
      lip=ip[-3:].lstrip('.')
      var = {}
      var['addr']=lip
      var['name']='SucPress1'
      var['index']= 42
      var['value']= 0
      var['Ident']=205
      var['Type']=2
      var['Unit']=56
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SucPress2'
      var['index']= 43
      var['value']= 0
      var['Ident']=206
      var['Type']=2
      var['Unit']=56
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SupHeat1'
      var['index']= 44
      var['value']= 0
      var['Ident']=207
      var['Type']=2
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SupHeat2'
      var['index']= 45
      var['value']= 0
      var['Ident']=208
      var['Type']=2
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='VFD_Hz'
      var['index']= 46
      var['value']= 0
      var['Ident']=209
      var['Type']=2
      var['Unit']=27
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Min_Comp1'
      var['index']= 47
      var['value']= 0
      var['Ident']= 210
      var['Type']=2
      var['Unit']=72
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Min_Comp2'
      var['index']= 48
      var['value']= 0
      var['Ident']= 211
      var['Type']=2
      var['Unit']=72
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='ModeNet'
      var['index']= 51
      var['value']= 0
      var['Ident']= 214
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='ActualHeatingSetpoint'
      var['index']= 53
      var['value']= 0
      var['Ident']= 216
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='ActualCoolingSetpoint'
      var['index']= 54
      var['value']= 0
      var['Ident']= 217
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='HeatingDemand'
      var['index']= 55
      var['value']= 0
      var['Ident']= 218
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='CoolingDemand'
      var['index']= 56
      var['value']= 0
      var['Ident']= 219
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='KwFan'
      var['index']= 64
      var['value']= 0
      var['Ident']=227
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Fan60HzKw'
      var['index']= 65
      var['value']= 0
      var['Ident']=228
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='FanKwReduction'
      var['index']= 67
      var['value']= 0
      var['Ident']=230
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='CompKwReduction'
      var['index']= 68
      var['value']= 0
      var['Ident']=231
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='TotalKwReduction'
      var['index']= 69
      var['value']= 0
      var['Ident']=232
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='TotalKwhReduction'
      var['index']= 70
      var['value']= 0
      var['Ident']=233
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='AveKwhReductionPerHour'
      var['index']= 71
      var['value']= 0
      var['Ident']=234
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='AveKwhUnitPerHour'
      var['index']= 72
      var['value']= 0
      var['Ident']=235
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='UnitKw'
      var['index']= 73
      var['value']= 0
      var['Ident']=236
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='FanSavingPercent'
      var['index']= 74
      var['value']= 0
      var['Ident']=237
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='FanKwhSaving'
      var['index']= 75
      var['value']= 0
      var['Ident']=238
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='CompKwhSaving'
      var['index']= 76
      var['value']= 0
      var['Ident']=239
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='UnitKwh'
      var['index']= 77
      var['value']= 0
      var['Ident']=240
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='FanRunHours'
      var['index']= 78
      var['value']= 0
      var['Ident']=241
      var['Type']=2
      var['Unit']=71
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp1RunHours'
      var['index']= 79
      var['value']= 0
      var['Ident']=242
      var['Type']=2
      var['Unit']=71
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp2RunHours'
      var['index']= 80
      var['value']= 0
      var['Ident']=243
      var['Type']=2
      var['Unit']=71
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='ScheduleStatus'
      var['index']= 88
      var['value']= 0
      var['Ident']=251
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp1_KW'
      var['index']= 103
      var['value']= 0
      var['Ident']=266
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Space_Hum'
      var['index']= 104
      var['value']= 0
      var['Ident']=267
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='OA_Hum'
      var['index']= 105
      var['value']= 0
      var['Ident']=268
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp2_kw'
      var['index']= 122
      var['value']= 0
      var['Ident']=285
      var['Type']=2
      var['Unit']=48
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='VSD_Fault'
      var['index']= 22
      var['value']= 0
      var['Ident']=23
      var['Type']=3
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Em_Shutdwn'
      var['index']= 23
      var['value']= 0
      var['Ident']=24
      var['Type']=3
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Filter'
      var['index']= 24
      var['value']= 0
      var['Ident']=25
      var['Type']=3
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='StartFan'
      var['index']= 30
      var['value']= 0
      var['Ident']=31
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Start Heater 1'
      var['index']= 31
      var['value']= 0
      var['Ident']=32
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Start Heater 2'
      var['index']= 32
      var['value']= 0
      var['Ident']=33
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Start Compresor 1'
      var['index']= 33
      var['value']= 0
      var['Ident']=34
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Start Compressor 2'
      var['index']= 34
      var['value']= 0
      var['Ident']=35
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='VSD_Enable'
      var['index']= 36
      var['value']= 0
      var['Ident']=37
      var['Type']=4
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='General_Alarm'
      var['index']= 49
      var['value']= 0
      var['Ident']= 212
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='High_SHeat_C1'
      var['index']= 50
      var['value']= 0
      var['Ident']= 213
      var['Type']=5
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Low_SHeat_C1'
      var['index']= 52
      var['value']= 0
      var['Ident']= 215
      var['Type']=5
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='HighPressC1'
      var['index']= 57
      var['value']= 0
      var['Ident']=220
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='LowPressC1'
      var['index']= 58
      var['value']= 0
      var['Ident']=221
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='High_SHeat_C2'
      var['index']= 59
      var['value']= 0
      var['Ident']=222
      var['Type']=5
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Low_SHeat_C2'
      var['index']= 60
      var['value']= 0
      var['Ident']=223
      var['Type']=5
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='HighPressC2'
      var['index']= 61
      var['value']= 0
      var['Ident']=224
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='LowPressC2'
      var['index']= 62
      var['value']= 0
      var['Ident']=225
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='HighSupplyTemp'
      var['index']= 63
      var['value']= 0
      var['Ident']=226
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='FanKwAlarm'
      var['index']= 66
      var['value']= 0
      var['Ident']=229
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Fan_Percent'
      var['index']= 128
      var['value']= 0
      var['Ident']=291
      var['Type']=2
      var['Unit']=98
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Occupy_Status'
      var['index']= 130
      var['value']= 0
      var['Ident']=293
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SPress1_Sensor_Fail'
      var['index']= 131
      var['value']= 0
      var['Ident']=294
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SPress2_Sensor_Fail'
      var['index']= 132
      var['value']= 0
      var['Ident']=295
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='STemp1_Sensor_Fail'
      var['index']= 133
      var['value']= 0
      var['Ident']=296
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='STemp2_Sensor_Fail'
      var['index']= 134
      var['value']= 0
      var['Ident']=297
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Coil_Temp_Sensor_Fail'
      var['index']= 135
      var['value']= 0
      var['Ident']=298
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Net_Status'
      var['index']= 136
      var['value']= 0
      var['Ident']=299
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Lim_Min_Alarm_SPress'
      var['index']= 123
      var['value']= 0
      var['Ident']=286
      var['Type']=2
      var['Unit']=56
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Lim_Max_Alarm_SPress'
      var['index']= 124
      var['value']= 0
      var['Ident']=287
      var['Type']=2
      var['Unit']=56
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='ForceMode'
      var['index']= 101
      var['value']= 0
      var['Ident']=264
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='TCoil1'
      var['index']= 0
      var['value']= 0
      var['Ident']=1
      var['Type']=0
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='TCoil2'
      var['index']= 2
      var['value']= 0
      var['Ident']=3
      var['Type']=0
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='LvtCoil'
      var['index']= 6
      var['value']= 0
      var['Ident']=7
      var['Type']=0
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='SaTemp'
      var['index']= 7
      var['value']= 0
      var['Ident']=8
      var['Type']=0
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Act_Outside_Temp'
      var['index']= 129
      var['value']= 0
      var['Ident']=292
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Current_ZnTemp'
      var['index']= 140
      var['value']= 0
      var['Ident']=303
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Lim_Min_SHeat_Alarm'
      var['index']= 125
      var['value']= 0
      var['Ident']=288
      var['Type']=2
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Lim_Max_SHeat_Alarm'
      var['index']= 126
      var['value']= 0
      var['Ident']=289
      var['Type']=2
      var['Unit']=120
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Lim_Coil_Temp_Alarm'
      var['index']= 127
      var['value']= 0
      var['Ident']=290
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Current_ZnCO2'
      var['index']= 145
      var['value']= 0
      var['Ident']=308
      var['Type']=2
      var['Unit']=96
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Fan_Speed_Status'
      var['index']= 150
      var['value']= 0
      var['Ident']=313
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp1_Status'
      var['index']= 151
      var['value']= 0
      var['Ident']=314
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Comp2_Status'
      var['index']= 152
      var['value']= 0
      var['Ident']=315
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Heat1_Status'
      var['index']= 153
      var['value']= 0
      var['Ident']=316
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Heat2_Status'
      var['index']= 154
      var['value']= 0
      var['Ident']=317
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Temp_Scale'
      var['index']= 155
      var['value']= 0
      var['Ident']=318
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Cool_Heat_Stat'
      var['index']= 157
      var['value']= 0
      var['Ident']=320
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='System_Mode'
      var['index']= 158
      var['value']= 0
      var['Ident']=321
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Act_ZnTemp_SP'
      var['index']= 159
      var['value']= 0
      var['Ident']=322
      var['Type']=2
      var['Unit']=64
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Total_Even_Kwh'
      var['index']= 162
      var['value']= 0
      var['Ident']=325
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Total_Odd_Kwh'
      var['index']= 163
      var['value']= 0
      var['Ident']=326
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Even_Counter'
      var['index']= 164
      var['value']= 0
      var['Ident']=327
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Odd_Counter'
      var['index']= 165
      var['value']= 0
      var['Ident']=328
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Saved_kWh'
      var['index']= 166
      var['value']= 0
      var['Ident']=329
      var['Type']=2
      var['Unit']=19
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='C1_Press_Prot'
      var['index']= 179
      var['value']= 0
      var['Ident']=342
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='C2_Press_Prot'
      var['index']= 180
      var['value']= 0
      var['Ident']=343
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Fan_Prot'
      var['index']= 181
      var['value']= 0
      var['Ident']=344
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='VSD_Alarm'
      var['index']= 186
      var['value']= 0
      var['Ident']=349
      var['Type']=5
      var['Unit']=95
      rtu_read_vars.append(var)
      var = {}
      var['addr']=lip
      var['name']='Total_Reset'
      var['index']= 187
      var['value']= 0
      var['Ident']=350
      var['Type']=2
      var['Unit']=95
      rtu_read_vars.append(var)
      
   

