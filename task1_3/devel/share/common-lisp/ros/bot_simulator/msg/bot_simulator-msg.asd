
(cl:in-package :asdf)

(defsystem "bot_simulator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "bot_pose" :depends-on ("_package_bot_pose"))
    (:file "_package_bot_pose" :depends-on ("_package"))
  ))