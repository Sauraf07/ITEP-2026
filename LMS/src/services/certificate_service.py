import os
from reportlab.pdfgen import canvas


class CertificateService:

    @staticmethod
    def generate_certificate():

        student_name = input(
            "Student Name : "
        )

        course_name = input(
            "Course Name : "
        )

        os.makedirs(
            "certificates",
            exist_ok=True
        )

        file_name = (
            f"certificates/"
            f"{student_name}_"
            f"{course_name}.pdf"
        )

        pdf = canvas.Canvas(file_name)

        pdf.setFont(
            "Helvetica-Bold",
            24
        )

        pdf.drawString(
            150,
            750,
            "CERTIFICATE"
        )

        pdf.setFont(
            "Helvetica",
            16
        )

        pdf.drawString(
            100,
            650,
            f"Presented To:"
        )

        pdf.drawString(
            250,
            650,
            student_name
        )

        pdf.drawString(
            100,
            600,
            f"For Successfully Completing:"
        )

        pdf.drawString(
            320,
            600,
            course_name
        )

        pdf.save()

        print(
            f"Certificate Generated:\n"
            f"{file_name}"
        )