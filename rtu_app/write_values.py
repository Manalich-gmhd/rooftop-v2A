from rtu_app.utility import get_value_syn, get_ip


def update_write_vars(rtu_write_vars):
   ip=get_ip()
   lip=ip[-3:].lstrip('.')
   for i in range(len(rtu_write_vars)):
      rtu_write_vars[i]['addr']=lip
      rsp=get_value_syn(rtu_write_vars[i]['index'])
      if rsp is not None:
            rtu_write_vars[i]['value']=float("{:.2f}".format(rsp))

def init_write_vars(rtu_write_vars):
      ip=get_ip()
      lip=ip[-3:].lstrip('.')
      var = {}
      var['addr']=21
      var['name']='OccupyOvrdDuration'
      var['index']= 39
      var['value']= 0
      var['Ident']=202
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OccCoolingSetpoint'
      var['index']= 40
      var['value']= 0
      var['Ident']=203
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OccHeatingSetpoint'
      var['index']= 41
      var['value']= 0
      var['Ident']=204
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='MinSpeedComp1'
      var['index']= 81
      var['value']= 0
      var['Ident']=244
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='MinSpeedComp2'
      var['index']= 82
      var['value']= 0
      var['Ident']=245
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='StartSpeed'
      var['index']= 84
      var['value']= 0
      var['Ident']=247
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='HeatSpeed'
      var['index']= 85
      var['value']= 0
      var['Ident']=248
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='WeekHourON'
      var['index']= 89
      var['value']= 0
      var['Ident']=252
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='WeekMinuteON'
      var['index']= 90
      var['value']= 0
      var['Ident']=253
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='WeekHourOFF'
      var['index']= 91
      var['value']= 0
      var['Ident']=254
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='WeekMinuteOFF'
      var['index']= 92
      var['value']= 0
      var['Ident']=255
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SundayHourON'
      var['index']= 93
      var['value']= 0
      var['Ident']=256
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SundayMinuteON'
      var['index']= 94
      var['value']= 0
      var['Ident']=257
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SundayHourOFF'
      var['index']= 95
      var['value']= 0
      var['Ident']=258
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SundayMinuteOFF'
      var['index']= 96
      var['value']= 0
      var['Ident']=259
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SaturdayHourON'
      var['index']= 97
      var['value']= 0
      var['Ident']=260
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SaturdayMinuteON'
      var['index']= 98
      var['value']= 0
      var['Ident']=261
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SaturdayHourOFF'
      var['index']= 99
      var['value']= 0
      var['Ident']=262
      var['Type']=2
      var['Unit']=71
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SaturdayMinuteOFF'
      var['index']= 100
      var['value']= 0
      var['Ident']=263
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='ForceMode'
      var['index']= 101
      var['value']= 0
      var['Ident']=264
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_SPress_Limit'
      var['index']= 107
      var['value']= 0
      var['Ident']=270
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_SPress_Limit'
      var['index']= 108
      var['value']= 0
      var['Ident']=271
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_SPress_Limit_ON'
      var['index']= 109
      var['value']= 0
      var['Ident']=272
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_SPress_Limit_ON'
      var['index']= 110
      var['value']= 0
      var['Ident']=273
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Total_Compressor'
      var['index']= 119
      var['value']= 0
      var['Ident']=282
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Minutes_Wait_ON'
      var['index']= 120
      var['value']= 0
      var['Ident']=283
      var['Type']=2
      var['Unit']=72
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OccupyViaNetwork'
      var['index']= 38
      var['value']= 0
      var['Ident']=201
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Fan_mode_speed'
      var['index']= 106
      var['value']= 0
      var['Ident']=269
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Lim_Min_Alarm_SPress'
      var['index']= 123
      var['value']= 0
      var['Ident']=286
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Lim_Max_Alarm_SPress'
      var['index']= 124
      var['value']= 0
      var['Ident']=287
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='EnableEvaluation'
      var['index']= 83
      var['value']= 0
      var['Ident']=246
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='EnableSpeedControl'
      var['index']= 86
      var['value']= 0
      var['Ident']=249
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='EnableSchedule'
      var['index']= 87
      var['value']= 0
      var['Ident']=250
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OATempOFF'
      var['index']= 102
      var['value']= 0
      var['Ident']=265
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Enable_Protection'
      var['index']= 121
      var['value']= 0
      var['Ident']=284
      var['Type']=5
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_STemp_Limit'
      var['index']= 111
      var['value']= 0
      var['Ident']=274
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_STemp_Limit'
      var['index']= 112
      var['value']= 0
      var['Ident']=275
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_STemp_Limit_ON'
      var['index']= 113
      var['value']= 0
      var['Ident']=276
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_STemp_Limit_ON'
      var['index']= 114
      var['value']= 0
      var['Ident']=277
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_Coil_Temp_Limit'
      var['index']= 115
      var['value']= 0
      var['Ident']=278
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_Coil_Temp_Limit'
      var['index']= 116
      var['value']= 0
      var['Ident']=279
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Low_Coil_Temp_Limit_ON'
      var['index']= 117
      var['value']= 0
      var['Ident']=280
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='High_Coil_Temp_Limit_ON'
      var['index']= 118
      var['value']= 0
      var['Ident']=281
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Lim_Min_SHeat_Alarm'
      var['index']= 125
      var['value']= 0
      var['Ident']=288
      var['Type']=2
      var['Unit']=120
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Lim_Max_SHeat_Alarm'
      var['index']= 126
      var['value']= 0
      var['Ident']=289
      var['Type']=2
      var['Unit']=120
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Lim_Coil_Temp_Alarm'
      var['index']= 127
      var['value']= 0
      var['Ident']=290
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Override_ZnTemp'
      var['index']= 138
      var['value']= 0
      var['Ident']=301
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='ZnTemp_Source'
      var['index']= 139
      var['value']= 0
      var['Ident']=302
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Override_ZnHum'
      var['index']= 141
      var['value']= 0
      var['Ident']=304
      var['Type']=2
      var['Unit']=98
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='ZnHum_Source'
      var['index']= 142
      var['value']= 0
      var['Ident']=305
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Override_ZnCO2'
      var['index']= 143
      var['value']= 0
      var['Ident']=306
      var['Type']=2
      var['Unit']=96
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='ZnCO2_Source'
      var['index']= 144
      var['value']= 0
      var['Ident']=307
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OATemp_Ovr'
      var['index']= 146
      var['value']= 0
      var['Ident']=309
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='OATemp_Mode'
      var['index']= 147
      var['value']= 0
      var['Ident']=310
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Unocc_Heating_SP'
      var['index']= 148
      var['value']= 0
      var['Ident']=311
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Unocc_Cooling_SP'
      var['index']= 149
      var['value']= 0
      var['Ident']=312
      var['Type']=2
      var['Unit']=64
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='SpaceHum_SP'
      var['index']= 160
      var['value']= 0
      var['Ident']=323
      var['Type']=2
      var['Unit']=98
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Space_CO2_SP'
      var['index']= 161
      var['value']= 0
      var['Ident']=324
      var['Type']=2
      var['Unit']=96
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Fan_Mode'
      var['index']= 156
      var['value']= 0
      var['Ident']=319
      var['Type']=2
      var['Unit']=95
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='CO2_Min_Speed'
      var['index']= 178
      var['value']= 0
      var['Ident']=341
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Max_Speed'
      var['index']= 183
      var['value']= 0
      var['Ident']=346
      var['Type']=2
      var['Unit']=27
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Suct_Press1_Offset'
      var['index']= 184
      var['value']= 0
      var['Ident']=347
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      var = {}
      var['addr']=21
      var['name']='Suct_Press2_Offset'
      var['index']= 185
      var['value']= 0
      var['Ident']=348
      var['Type']=2
      var['Unit']=56
      rtu_write_vars.append(var)
      