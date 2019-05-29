Sub SampleCall()
    mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
    RunPython ("import " & mymodule & ";" & mymodule & ".hello_xlwings()")
End Sub


Sub Analyze()
    'FILE-SIDE PREPARATION
    'Returns file path string or boolean false
    vFile = Application.GetOpenFilename(Title:="Select File To Be Opened")
    
    'Error handling; easier to handle out of getWorkbook
    If vFile = False Then
        MsgBox ("Verification Cancelled.")
        Exit Sub
    Else
        'replace / with // to avoid unicode decoding errors
        sFile = "'" & Replace(CStr(vFile), "\", "//") & "'"
        
    End If
    
    mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
    
    RunPython ("import " & mymodule & "; " & mymodule & ".main(" & sFile & ")")

End Sub
