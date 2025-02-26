const mic_btn = document.getElementById("voice-btn");

let can_record = false;
let is_recording = false;
let recorder = null;
let chunks = [];

function SetupAudio() {
  console.log("setup started");
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
      .getUserMedia({
        audio: true,
      })
      .then(SetupStream)
      .catch((err) => {
        console.error(err);
      });
  }
}

function SetupStream(stream) {
  console.log("stream started")
  recorder = new MediaRecorder(stream);

  recorder.ondataavailable = (e) => {
    chunks.push(e.data);
  };

  recorder.onstop = async (e) => {
    const blob = new Blob(chunks, { type: "audio/wav" });
    chunks = [];
    const audioURL = window.URL.createObjectURL(blob);

    await uploadAudio(blob);
  };

  can_record = true;
}

function ToggleMic() {
  if (!can_record) return;

  is_recording = !is_recording;
  if (is_recording) {
    recorder.start();
  } else {
    recorder.stop();
  }
}

async function uploadAudio(blob) {
  console.log("Uploading audio file...");
  const formData = new FormData();
  formData.append("file", blob, "speech.wav");
  
  try {
    const response = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData,
    });
    
    if (!response.ok) {
      throw new Error(`Server returned ${response.status}: ${response.statusText}`);
    }
    
    const result = await response.json();
    console.log("Server response:", result);
    return result;
  } catch (error) {
    console.error("Upload error:", error);
    alert("Failed to upload audio. See console for details.");
  }
}

window.addEventListener("DOMContentLoaded", () => {
  if (!mic_btn) {
    console.error("Microphone button not found! Make sure element with ID 'voice-btn' exists.");
    return;
  }
  
  mic_btn.addEventListener("click", ToggleMic);
  SetupAudio();
});

