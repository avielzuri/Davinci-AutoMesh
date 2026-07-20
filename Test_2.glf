# Fidelity Pointwise 2024.2.3 Journal file - Thu Jul 16 13:41:19 2026

package require PWI_Glyph 8.24.2

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}

pw::Application clearModified

set _TMP(mode_1) [pw::Application begin DatabaseImport]
  $_TMP(mode_1) initialize -strict -type Automatic {C:/Users/joojo/Desktop/Summer Research/CAD FIles/P088_T121_R103_B1_TEST2.STEP}
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Database}

pw::Connector setCalculateDimensionMethod Spacing
pw::Connector setCalculateDimensionSpacing 0.29999999999999999
set _DB(1) [pw::DatabaseEntity getByName Combine2]
set _TMP(PW_1) [pw::DomainStructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

pw::Application undo
pw::Application setGridPreference Unstructured
set _TMP(PW_1) [pw::DomainUnstructured createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Domains On DB Entities}

