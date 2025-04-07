from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

# Download punkt tokenizer if not already present
nltk.download('punkt')
nltk.download('punkt_tab')

def split_into_chunks(text, max_chunk_words=500):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        if len(' '.join(current_chunk + [sentence]).split()) <= max_chunk_words:
            current_chunk.append(sentence)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def summarize_text(text, num_paragraphs=3):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn" ,framework="pt")

    chunks = split_into_chunks(text, max_chunk_words=700)
    summarized_chunks = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]

    # Combine all summarized parts and split for final output
    final_summary = ' '.join(summarized_chunks)
    sentences = sent_tokenize(final_summary)

    # Split summary into desired number of paragraphs
    avg_sent_per_para = max(1, len(sentences) // num_paragraphs)
    paragraphs = [' '.join(sentences[i:i+avg_sent_per_para]) for i in range(0, len(sentences), avg_sent_per_para)]

    return '\n\n'.join(paragraphs[:num_paragraphs])

# Example usage:
if __name__ == "__main__":
    large_text = """Executive Summary: This online service, based in Nairobi, Kenya, aims to connect vehicle owners with professional mechanics through a GPS-enabled mobile application. The goal is to simplify the process of finding nearby mechanics, ensuring quick and reliable car repairs whenever breakdowns occur. The app will feature a verification process for mechanics, ensuring professionalism and quality service through physical assessments.
Kenya’s automotive industry is growing, and with an increasing number of vehicles on the road, breakdowns are inevitable. However, car owners often struggle to find reliable mechanics, especially in urgent situations. This business intends to bridge this gap by providing a digital solution that prioritizes convenience, professionalism, and accessibility. Through this app, vehicle owners will be able to locate verified mechanics based on proximity, ensuring faster service and reduced waiting times. Our vision is to become the leading online platform for automotive repair services in Kenya, offering quality, reliability, and affordability.
Business Description: This mobile application will serve as an online platform where vehicle owners can easily locate and request services from nearby professional mechanics. The app will feature GPS integration to show mechanics closest to the user, along with their ratings, reviews, and pricing. Mechanics will be required to undergo a verification process to ensure they meet professional standards.
The service will be accessible via a mobile app and website, making it convenient for customers to find and book mechanics anytime, anywhere. Multiple payment options, including mobile money (M-Pesa), credit/debit cards, and cash payments, will be available. The platform will also feature emergency roadside assistance for users who experience breakdowns in remote locations.
Operation Plan:
•	App Development: Build and maintain a user-friendly mobile application with GPS tracking, secure payment processing, and user profiles for both customers and mechanics.
•	Mechanic Verification: Conduct physical assessments and background checks to ensure only skilled and reliable professionals are listed.
•	Service Request System: Implement an easy-to-use booking system that allows customers to request services and receive real-time updates.
•	Customer Support: Establish a 24/7 support team to assist users and handle disputes between mechanics and clients.
•	Security Measures: Implement strict data protection policies and secure payment gateways to safeguard customer transactions and personal information.
Organization Management: The business will operate under a structured management framework with the following key roles:
•	Chief Executive Officer (CEO): Overseeing business operations and strategic planning.
•	Chief Technology Officer (CTO): Managing app development, cybersecurity, and technological innovations.
•	Operations Manager: Handling mechanic onboarding, verification, and service quality control.
•	Marketing Manager: Developing and implementing marketing strategies to attract users and mechanics.
•	Customer Support Team: Addressing customer inquiries, complaints, and dispute resolutions.
•	Finance Manager: Managing financial planning, budgeting, and financial reporting.
Legal Structure of the Business: This business will be registered as a Private Limited Company (PLC) under the Companies Act of Kenya. It will comply with all legal and regulatory requirements, including:
•	Acquiring a business permit from Nairobi County Government.
•	Registering with the Kenya Revenue Authority (KRA) for tax compliance.
•	Ensuring adherence to data protection laws and consumer rights regulations.
•	Complying with relevant transport and road service authorities.
•	Implementing clear terms of service agreements for both mechanics and customers.
Products and Services:
•	Mechanic Locator: GPS-based search to find nearby mechanics quickly.
•	Service Categories: General car servicing, emergency breakdown repairs, towing services, and specialized auto repairs.
•	Verification and Rating System: Customer reviews, ratings, and professional assessments for mechanics.
•	Emergency Roadside Assistance: Immediate help for users in case of vehicle breakdowns.
•	Multiple Payment Options: M-Pesa, credit/debit cards, and cash payments.
•	Subscription Services: Premium users can access additional benefits, such as priority service and discounted rates.
Marketing and Sales Strategy:
•	Digital Marketing: Utilize social media advertising, SEO, and Google Ads to reach a broad audience and drive app downloads.
•	Partnerships: Collaborate with taxi companies, car rental services, and insurance firms to increase visibility.
•	Referral Programs: Offer incentives for customers who refer new users to the platform.
•	Brand Ambassadors: Work with influencers and automotive experts to promote the service.
•	Customer Retention Strategies: Implement loyalty programs and exclusive discounts for returning customers.
Competitive Analysis:
•	Direct Competitors: Existing mechanic directory services and informal roadside mechanics.
•	Strengths: Verified professionals, convenient booking system, fast response times, and secure payment options.
•	Weaknesses: Initial challenges in attracting mechanics and customers to use the platform.
•	Opportunities: The increasing adoption of mobile applications for service-based businesses in Kenya.
•	Threats: Resistance from traditional mechanics who may be skeptical about using digital platforms.
Unique Selling Proposition: This business will stand out by offering:
•	Verified Mechanics: Ensuring trust and quality through professional assessments.
•	Real-Time GPS Matching: Connecting car owners with the nearest available mechanic instantly.
•	Emergency Services: Providing 24/7 roadside assistance for breakdowns.
•	Secure Transactions: Implementing safe and seamless digital payment options.
•	Customer Support: A dedicated team to resolve issues and enhance user experience.
Financial Plan:
•	Initial Investment: Approx. Ksh 4 million for app development, marketing, operations, and verification processes.
•	Revenue Model:
o	Service commission charged on each transaction.
o	Subscription-based premium features for mechanics and customers.
o	Advertising revenue from auto service businesses and spare part dealers.
o	Emergency roadside assistance membership plans.
•	Projected Revenue:
o	Year 1: Ksh 5 million.
o	Year 2: Ksh 8 million.
o	Year 3: Ksh 12 million.
•	Break-Even Analysis: Expected within 18-24 months of operation.
"""
    result = summarize_text(large_text, num_paragraphs=3)
    print(result)
