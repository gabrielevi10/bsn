#ifndef STATUS_MESSAGE_HPP
#define STATUS_MESSAGE_HPP

#include <string>

class StatusMessage {

  	public:
		StatusMessage(const std::string &name, 
                        const int64_t &timestamp, 
                        const int64_t &logical_clock, 
                        const std::string &source, 
                        const std::string &target, 
                        const std::string &state,
                        const double &global_reli) : 
                        name(name), 
                        timestamp(timestamp), logical_clock(logical_clock), source(source), target(target), state(state), global_reli(global_reli) {};
        
        std::string getName() const { return this->name;};
        int64_t getTimestamp() const {return this->timestamp;};
        int64_t getLogicalClock() const {return this->logical_clock;};
        std::string getSource() const {return this->source;};
        std::string getTarget() const {return this->target;};
        std::string getState() const {return this->state;};
        double getReli() const { return this->global_reli;};    
	private:
        std::string name;
        int64_t timestamp;
        int64_t logical_clock;
        std::string source;
        std::string target;
        std::string state;
        double global_reli;
};

#endif 