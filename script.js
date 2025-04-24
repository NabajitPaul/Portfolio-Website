document.addEventListener("DOMContentLoaded", () => {
  // Contact form submission
  const contactForm = document.getElementById("contact-form")
  const formMessage = document.getElementById("form-message")

  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault()

      // Get form data
      const formData = new FormData(contactForm)
      const submitBtn = contactForm.querySelector(".submit-btn")

      // Change button text and disable it
      submitBtn.textContent = "Sending..."
      submitBtn.disabled = true

      // Send form data to backend
      fetch("/submit-form", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          formMessage.textContent = data.message
          if (data.success) {
            contactForm.reset()
          }
        })
        .catch((error) => {
          console.error("Error:", error)
          formMessage.textContent = "Something went wrong. Please try again."
        })
        .finally(() => {
          // Reset button
          submitBtn.textContent = "Send Message"
          submitBtn.disabled = false
        })
    })
  }

  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault()

      const targetId = this.getAttribute("href")
      const targetElement = document.querySelector(targetId)

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 70, // Adjust for header height
          behavior: "smooth",
        })
      }
    })
  })

  // Mobile navigation toggle (if needed)
  // This would be implemented if we had a mobile menu button

  // Optional: Dark mode toggle
  // This would be implemented if we had a dark mode toggle button
})
