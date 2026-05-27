document.addEventListener("DOMContentLoaded", () => {
    const wrapper = document.querySelector(".astronaut-wrapper");
    const header = document.querySelector("header");
  
    function moveAstronautRandomly() {
      const maxX = header.clientWidth - wrapper.clientWidth;
      const maxY = header.clientHeight - wrapper.clientHeight;
  
      const randomX = Math.random() * maxX;
      const randomY = Math.random() * maxY;
  
      wrapper.style.transform = `translate(${randomX}px, ${randomY}px)`;
    }
  
    setInterval(moveAstronautRandomly, 2000);
  });
  