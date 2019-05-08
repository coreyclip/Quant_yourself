Sub Verification_Report()
    'FILE-SIDE PREPARATION
    'Returns file path string or boolean false
    vFile = Application.GetOpenFilename(FileFilter:="Excel Workbooks (*.XLSX), *.XLSX", Title:="Select File To Be Opened")
    
    'Error handling; easier to handle out of getWorkbook
    If vFile = False Then
        MsgBox ("Verification Cancelled.")
        Exit Sub
    Else
        'replace / with // to avoid unicode decoding errors
        sFile = "'" & Replace(CStr(vFile), "\", "//") & "'"
        
    End If
    
    mymodule = Left(ThisWorkbook.name, (InStrRev(ThisWorkbook.name, ".", -1, vbTextCompare) - 1))
    
    RunPython ("import " & mymodule & "; " & mymodule & ".main(" & sFile & ")")

End Sub