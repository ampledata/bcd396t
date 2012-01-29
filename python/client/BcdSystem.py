# This code contains Uniden proprietary and/or copyright control codes. Used with permission.

class BcdInfo:
	def from_bcd(self, index, bcd_string):
		self.index = index
		self.bcd_data = bcd_string.split(',')

	def to_s(self):
		return ','.join(self.bcd_data)

class BcdSystem:
	pass

class BcdSystemInfo(BcdInfo):
	#SIN,[SYS_TYPE],[NAME],[QUICK_KEY],[HLD],[LOUT],[DLY],[SKP],[MOD],[ATT],[APCO],[THRESHOLD],[REV_INDEX],[FWD_INDEX],[CHN_GRP_HEAD],[CHN_GRP_TAIL],[SEQ_NO][\r]
	#SIN,5285
	#SIN,M82S,Baltimore County,1,2,0,2,,AUTO,0,AUTO,8,-1,5166,5287,5287,4
	pass

class BcdGroupInfo(BcdInfo):
	#GIN,[GRP_TYPE],[NAME],[QUICK_KEY],[LOUT],[REV_INDEX],[FWD_INDEX],[SYS_INDEX],[C HN_HEAD],[CHN_TAIL],[SEQ_NO][\r]
	#GIN,5287
	#GIN,C,System Frequency,.,0,-1,-1,5285,5289,5292,1
	pass

class BcdTrunkFrequencyInfo(BcdInfo):
	#TFQ,[FRQ],[LCN],[LOUT],[REV_INDEX],[FWD_INDEX],[SYS_INDEX],[GRP_INDEX][\r]
	#TFQ,5289
	#TFQ,08579625,,0,-1,5290,5285,5287
	#TFQ,5290
	#TFQ,08589625,,0,5289,5291,5285,5287
	#TFQ,5291
	#TFQ,08599625,,0,5290,5292,5285,5287
	#TFQ,5292
	#TFQ,08609625,,0,5291,-1,5285,5287
	pass

class BcdTrunkInfo(BcdInfo):
	#TRN,[ID_SEARCH],[S_BIT],[END_CODE],[AFS],[I-CALL],[C-CH],[EMG],[EMGL],[FMAP],[CTM_FMAP],[BASE1],[STEP1],[OFFSET1],[BASE2],[STEP2],[OFFSET2],[BASE3],[STEP3], [OFFSET3],[MFID],[TGID_GRP_HEAD],[TGID_GRP_TAIL],[ID_LOUT_GRP_HEAD], [ID_LOUT_GRP_TAIL][\r]
	#TRN,0,0,1,,1,1,7,0,16,00000000,,,,,,,,,,0,5293,5857,5288,5288
	pass

class BcdSystemGroupInfo(BcdInfo):
	#GIN,[GRP_TYPE],[NAME],[QUICK_KEY],[LOUT],[REV_INDEX],[FWD_INDEX],[SYS_INDEX],[C HN_HEAD],[CHN_TAIL],[SEQ_NO][\r]
	#GIN,5293
	#GIN,T,Parkville,1,0,-1,5297,5285,5294,5296,1
	#GIN,5297
	#GIN,T,Towson,2,0,5293,5301,5285,5298,5300,2
	#...
	#GIN,5857
	#GIN,T,Qck Save Grp,.,0,5399,-1,5285,5858,5858,10
	pass

class BcdSystemGroupTalkInfo(BcdInfo):
	#TIN,[NAME],[TGID],[LOUT],[PRI],[ALT],[ALTL],[REV_INDEX],[FWD_INDEX], [SYS_INDEX],[GRP_INDEX][\r]
	#TIN,5294
	#TIN,Dispatch 08,1840,0,0,0,0,-1,5295,5285,5293
	#TIN,5295
	#TIN,Tactical 08,2288,0,0,0,0,5294,5296,5285,5293
	#TIN,5296
	#TIN,ISU 08,7728,0,0,0,0,5295,-1,5285,5293
	pass

class BcdQuickGroupsInfo(BcdInfo):
	#QGL,##########[\r]
	#QGL,5285
	#QGL,2222221110
	pass


