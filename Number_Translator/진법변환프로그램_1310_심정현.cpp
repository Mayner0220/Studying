#include <stdio.h>
#define ERR -2
int trans(char *from, int demical); // convert input to demical number function
void converter(int result, int re); // convert demical number function

int main(){
	int demical, result, re;
	char from[30];
	while(1){
		printf("[����]\n>> ");
		scanf("%d", &demical);
		printf("\nSaved ����: %d\n", demical);
		printf("\n[��ȯ �� �Է°�]\n>> ");
		if(demical==2||demical==8||demical==10||demical==16){ // ���� �Է°� ���� 
			scanf("%s", from);
			printf("\n[��ȯ�� ����]\n>> ");
			scanf("%d", &re);
			result=trans(from, demical);
			if(result<0){
				printf("\nInput Error");
				return 0; 
			}
			converter(result, re);
		}
		else{
			printf("\nInput Error");
			return 0;
		}
	}
	return 0;
}

int trans(char *from, int demical){
	int temp=0, i;
	for(i=0;from[i]!='\0';i++){
		if(from[i]>='0'&&from[i]<='9'){ // �Է°��� 0~9�� �� 10������ ��ȯ 
			from[i]-='0';
		}
		else if(from[i]>='A'&&from[i]<='F'){ // �Է°��� A~F�� �� 10������ ��ȯ 
			from[i]-='A';
			from[i]+=10;
		}
		if(from[i]>=demical) return ERR; // check the input error
		temp*=demical; // ���� ��ȯ �ڵ� 
		temp+=from[i];
		if(temp>65535) return ERR; // check the input error
	}
	return temp;
}

void converter(int result, int re){
	int i, m=28;
	char changed[30];
	for(i=0;i<30;i++){
		changed[i]=-1; // ��ȯ���� ������ �迭�� -1�� �ʱ�ȭ 
	}
	for(i=re;result>0;){
		changed[m--]=result%re; // �Է� ���� ������ ��ȯ�ϴ� �ڵ� 
		result/=re;
	}
	printf("\n���: "); 
	for(i=m+1;changed[i]!=-1;i++){  
		if(changed[i]>=0&&changed[i]<=9){ // ��ȯ�� ���� 0~9�� �� ��ȯ �ڵ� 
			changed[i]+='0';
		}
		else if(changed[i]>=10&&changed[i]<=15){ // ��ȯ�� ���� A~F�� �� ��ȯ �ڵ� 
			changed[i]-=10;
			changed[i]+='A';
		}
		printf("%c", changed[i]);
	}
	printf("\n\n");
}
