(fn print-sep [sep ...]
  "Prints args as a string, delimited by sep"
  (print (table.concat [...] sep)))
,doc print-sep ; -> outputs:
;; (print-sep sep ...)
;;   Prints args as a string, delimited by sep:Fnl (print "hey")
