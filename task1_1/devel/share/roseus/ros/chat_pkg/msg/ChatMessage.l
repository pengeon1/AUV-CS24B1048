;; Auto-generated. Do not edit!


(when (boundp 'chat_pkg::ChatMessage)
  (if (not (find-package "CHAT_PKG"))
    (make-package "CHAT_PKG"))
  (shadow 'ChatMessage (find-package "CHAT_PKG")))
(unless (find-package "CHAT_PKG::CHATMESSAGE")
  (make-package "CHAT_PKG::CHATMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude ChatMessage.msg.html


(defclass chat_pkg::ChatMessage
  :super ros::object
  :slots (_sender _message ))

(defmethod chat_pkg::ChatMessage
  (:init
   (&key
    ((:sender __sender) "")
    ((:message __message) "")
    )
   (send-super :init)
   (setq _sender (string __sender))
   (setq _message (string __message))
   self)
  (:sender
   (&optional __sender)
   (if __sender (setq _sender __sender)) _sender)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; string _sender
    4 (length _sender)
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _sender
       (write-long (length _sender) s) (princ _sender s)
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _sender
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _sender (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get chat_pkg::ChatMessage :md5sum-) "985ef42f02a992c58d5de728edeb121e")
(setf (get chat_pkg::ChatMessage :datatype-) "chat_pkg/ChatMessage")
(setf (get chat_pkg::ChatMessage :definition-)
      "string sender
string message

")



(provide :chat_pkg/ChatMessage "985ef42f02a992c58d5de728edeb121e")


