import Header from "@/components/Header";
import Hero from "@/components/Hero";
import Features from "@/components/Features";
import Statistics from "@/components/Statistics";
import PricingCards from "@/components/PricingCards";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen">
      <Header />
      <Hero />
      <Features />
      <Statistics />
      <PricingCards />
      <Footer />
    </div>
  );
};

export default Index;
