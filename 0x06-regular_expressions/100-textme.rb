#!/usr/bin/env ruby
<<<<<<< HEAD
#hello
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
=======
sender =  ARGV[0].scan(/(?<=from:)(.*?)(?=\])/).join
receiver = ARGV[0].scan(/(?<=to:)(.*?)(?=\])/).join
flags = ARGV[0].scan(/(?<=flags:)(.*?)(?=\])/).join
result = sender + "," + receiver + "," + flags
puts result
>>>>>>> ed7aa87c1a3a1796754a3fe2b83d783f0d9ac7b3
