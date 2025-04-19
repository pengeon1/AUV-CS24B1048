;; Auto-generated. Do not edit!


(when (boundp 'bot_simulator::bot_pose)
  (if (not (find-package "BOT_SIMULATOR"))
    (make-package "BOT_SIMULATOR"))
  (shadow 'bot_pose (find-package "BOT_SIMULATOR")))
(unless (find-package "BOT_SIMULATOR::BOT_POSE")
  (make-package "BOT_SIMULATOR::BOT_POSE"))

(in-package "ROS")
;;//! \htmlinclude bot_pose.msg.html


(defclass bot_simulator::bot_pose
  :super ros::object
  :slots (_x _y _facing ))

(defmethod bot_simulator::bot_pose
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:facing __facing) "")
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _facing (string __facing))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:facing
   (&optional __facing)
   (if __facing (setq _facing __facing)) _facing)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; string _facing
    4 (length _facing)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _facing
       (write-long (length _facing) s) (princ _facing s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _facing
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _facing (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get bot_simulator::bot_pose :md5sum-) "d7659f9c689cfd66a9a6fb85b21deb2b")
(setf (get bot_simulator::bot_pose :datatype-) "bot_simulator/bot_pose")
(setf (get bot_simulator::bot_pose :definition-)
      "float32 x
float32 y
string facing

")



(provide :bot_simulator/bot_pose "d7659f9c689cfd66a9a6fb85b21deb2b")


