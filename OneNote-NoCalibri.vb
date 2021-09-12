$cnFont = "等线"
$enFont = "DengXian"
$badFont = "Calibri"
$fontSize = 14

ForEach ($pre in QueryObjects("Text", GetCurrentPage()))
  If($pre.fontName == $badFont)
    If(String_LessThan($pre.value, Chr(255), false) && String_GreaterThan($pre.value, Chr(0), false))
      $pre.fontName = $enFont
    Else
      $pre.fontName = $cnFont
    $pre.fontSize = $fontSize